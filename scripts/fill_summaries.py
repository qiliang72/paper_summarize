from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from paper_app.config import PAPERS_STORE_PATH
from paper_app.paper_store import read_paper_store, write_paper_store
from scripts.summarize_gemini import summarize_papers


def fill_summaries(
    store_path: Path = PAPERS_STORE_PATH,
    offline: bool = False,
    delay_seconds: float = 5,
    retry_count: int = 2,
    retry_delay_seconds: float = 30,
    limit: int | None = None,
    failure_threshold: int = 2,
    verbose: bool = True,
) -> list[dict]:
    papers = read_paper_store(store_path)
    summarized = summarize_papers(
        papers,
        offline=offline,
        delay_seconds=delay_seconds,
        retry_count=retry_count,
        retry_delay_seconds=retry_delay_seconds,
        limit=limit,
        failure_threshold=failure_threshold,
        verbose=verbose,
    )
    write_paper_store(summarized, store_path)
    return summarized


def main() -> int:
    parser = argparse.ArgumentParser(description="Fill missing Chinese translations and summaries in the long-term paper store.")
    parser.add_argument("--store", type=Path, default=PAPERS_STORE_PATH)
    parser.add_argument("--offline", action="store_true", help="Skip Gemini calls and generate fallback summaries.")
    parser.add_argument("--delay-seconds", type=float, default=float(os.getenv("GEMINI_DELAY_SECONDS", "5")))
    parser.add_argument("--retry-count", type=int, default=int(os.getenv("GEMINI_RETRY_COUNT", "2")))
    parser.add_argument("--retry-delay-seconds", type=float, default=float(os.getenv("GEMINI_RETRY_DELAY_SECONDS", "30")))
    parser.add_argument("--limit", type=int, default=None, help="Maximum number of incomplete papers to generate in this run.")
    parser.add_argument("--failure-threshold", type=int, default=int(os.getenv("GEMINI_FAILURE_THRESHOLD", "2")))
    parser.add_argument("--quiet", action="store_true", help="Hide per-paper progress output.")
    args = parser.parse_args()

    before = read_paper_store(args.store)
    missing_before = sum(1 for paper in before if not paper.get("abstract_zh") or not paper.get("summary_zh"))
    summarized = fill_summaries(
        args.store,
        offline=args.offline,
        delay_seconds=args.delay_seconds,
        retry_count=args.retry_count,
        retry_delay_seconds=args.retry_delay_seconds,
        limit=args.limit,
        failure_threshold=args.failure_threshold,
        verbose=not args.quiet,
    )
    missing_after = sum(1 for paper in summarized if not paper.get("abstract_zh") or not paper.get("summary_zh"))
    print(f"Processed {missing_before} incomplete records. Remaining incomplete records: {missing_after}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
