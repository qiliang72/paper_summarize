from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from paper_app.config import CLASSIFIED_PAPERS_PATH, ROOT_DIR, SUMMARIZED_PAPERS_PATH, load_config
from paper_app.storage import read_json, write_json

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

try:
    from pydantic import BaseModel, ConfigDict, Field
except ImportError:
    BaseModel = None
    ConfigDict = None
    Field = None


if BaseModel is not None:

    class PaperSummary(BaseModel):
        model_config = ConfigDict(extra="forbid")

        abstract_zh: str = Field(description="忠实翻译英文摘要为中文。")
        summary_zh: str = Field(description="用中文写 2-3 句话的简短总结。")

else:

    class PaperSummary:
        def __init__(self, abstract_zh: str, summary_zh: str):
            self.abstract_zh = abstract_zh
            self.summary_zh = summary_zh

        @classmethod
        def model_json_schema(cls) -> dict:
            return {
                "type": "object",
                "properties": {
                    "abstract_zh": {
                        "type": "string",
                        "description": "忠实翻译英文摘要为中文。",
                    },
                    "summary_zh": {
                        "type": "string",
                        "description": "用中文写 2-3 句话的简短总结。",
                    },
                },
                "required": ["abstract_zh", "summary_zh"],
                "additionalProperties": False,
            }

        @classmethod
        def model_validate_json(cls, value: str) -> "PaperSummary":
            data = json.loads(value)
            return cls(
                abstract_zh=str(data.get("abstract_zh", "")),
                summary_zh=str(data.get("summary_zh", "")),
            )


def _fallback_summary(abstract: str) -> PaperSummary:
    compact = " ".join(abstract.split())
    preview = compact[:260] + ("..." if len(compact) > 260 else "")
    return PaperSummary(
        abstract_zh="",
        summary_zh=f"Gemini 总结暂不可用。英文摘要要点预览：{preview}",
    )


def summarize_one(client, model: str, paper: dict) -> PaperSummary:
    prompt = (
        "请阅读下面的 arXiv 论文信息，完成两个字段：\n"
        "1. abstract_zh: 忠实翻译英文摘要为中文。\n"
        "2. summary_zh: 用中文写 2-3 句话，概括问题、方法和主要贡献。\n"
        "不要夸大论文结论，不要添加原文没有的信息。\n\n"
        f"Title: {paper.get('title', '')}\n"
        f"Abstract: {paper.get('abstract_en', '')}"
    )
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_json_schema": PaperSummary.model_json_schema(),
        },
    )
    return PaperSummary.model_validate_json(response.text)


def _is_retryable_error(exc: Exception) -> bool:
    message = str(exc)
    return "429" in message or "503" in message or "RESOURCE_EXHAUSTED" in message or "UNAVAILABLE" in message


def _summarize_with_retries(client, model: str, paper: dict, retry_count: int, retry_delay_seconds: float) -> PaperSummary:
    last_exc: Exception | None = None
    for attempt in range(retry_count + 1):
        try:
            return summarize_one(client, model, paper)
        except Exception as exc:
            last_exc = exc
            if attempt >= retry_count or not _is_retryable_error(exc):
                raise
            wait_seconds = retry_delay_seconds * (attempt + 1)
            print(
                f"[retry] {paper.get('arxiv_id', 'unknown')} failed with {type(exc).__name__}; "
                f"waiting {wait_seconds:g}s before retry {attempt + 1}/{retry_count}.",
                flush=True,
            )
            time.sleep(wait_seconds)
    raise RuntimeError("Unexpected summary retry state.") from last_exc


def summarize_papers(
    papers: list[dict],
    offline: bool = False,
    delay_seconds: float = 0,
    retry_count: int = 2,
    retry_delay_seconds: float = 30,
    limit: int | None = None,
    verbose: bool = True,
) -> list[dict]:
    if load_dotenv is not None:
        load_dotenv(ROOT_DIR / ".env")
    config = load_config()
    api_key = os.getenv("GEMINI_API_KEY")

    client = None
    if not offline and api_key:
        try:
            from google import genai

            client = genai.Client(api_key=api_key)
        except ImportError as exc:
            raise RuntimeError("Missing dependency: install requirements.txt before summarizing papers.") from exc

    summarized = []
    generated_count = 0
    total = len(papers)
    for index, paper in enumerate(papers, start=1):
        updated = dict(paper)
        arxiv_id = updated.get("arxiv_id", "unknown")
        if updated.get("abstract_zh") and updated.get("summary_zh"):
            if verbose:
                print(f"[{index}/{total}] skip {arxiv_id}: Chinese fields already complete.", flush=True)
            summarized.append(updated)
            continue

        if limit is not None and generated_count >= limit:
            if verbose:
                print(f"[{index}/{total}] defer {arxiv_id}: run limit {limit} reached.", flush=True)
            summarized.append(updated)
            continue

        try:
            if client is None:
                if verbose:
                    print(f"[{index}/{total}] fallback {arxiv_id}: Gemini client unavailable.", flush=True)
                summary = _fallback_summary(updated.get("abstract_en", ""))
                if not offline and not api_key:
                    updated["summary_error"] = "GEMINI_API_KEY is not set; used fallback summary."
            else:
                if generated_count > 0 and delay_seconds > 0:
                    if verbose:
                        print(f"[{index}/{total}] wait {delay_seconds:g}s before {arxiv_id}.", flush=True)
                    time.sleep(delay_seconds)
                if verbose:
                    print(f"[{index}/{total}] generate {arxiv_id} with Gemini.", flush=True)
                summary = _summarize_with_retries(client, config.gemini_model, updated, retry_count, retry_delay_seconds)
                updated.pop("summary_error", None)
            updated["abstract_zh"] = summary.abstract_zh
            updated["summary_zh"] = summary.summary_zh
            generated_count += 1
            if verbose:
                print(f"[{index}/{total}] done {arxiv_id}.", flush=True)
        except Exception as exc:
            updated["summary_error"] = str(exc)
            if verbose:
                print(f"[{index}/{total}] error {arxiv_id}: {exc}", flush=True)
            fallback = _fallback_summary(updated.get("abstract_en", ""))
            updated["abstract_zh"] = updated.get("abstract_zh", "")
            updated["summary_zh"] = fallback.summary_zh
        summarized.append(updated)
    return summarized


def main() -> int:
    parser = argparse.ArgumentParser(description="Translate and summarize paper abstracts with Gemini.")
    parser.add_argument("--input", type=Path, default=CLASSIFIED_PAPERS_PATH)
    parser.add_argument("--output", type=Path, default=SUMMARIZED_PAPERS_PATH)
    parser.add_argument("--offline", action="store_true", help="Skip Gemini calls and generate fallback summaries.")
    parser.add_argument("--delay-seconds", type=float, default=float(os.getenv("GEMINI_DELAY_SECONDS", "0")))
    parser.add_argument("--retry-count", type=int, default=int(os.getenv("GEMINI_RETRY_COUNT", "2")))
    parser.add_argument("--retry-delay-seconds", type=float, default=float(os.getenv("GEMINI_RETRY_DELAY_SECONDS", "30")))
    parser.add_argument("--limit", type=int, default=None, help="Maximum number of incomplete papers to generate in this run.")
    parser.add_argument("--quiet", action="store_true", help="Hide per-paper progress output.")
    args = parser.parse_args()

    papers = read_json(args.input, [])
    summarized = summarize_papers(
        papers,
        offline=args.offline,
        delay_seconds=args.delay_seconds,
        retry_count=args.retry_count,
        retry_delay_seconds=args.retry_delay_seconds,
        limit=args.limit,
        verbose=not args.quiet,
    )
    write_json(args.output, summarized)
    print(f"Wrote {len(summarized)} summarized papers to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
