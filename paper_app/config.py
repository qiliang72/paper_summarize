from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
DOCS_DIR = ROOT_DIR / "docs"
RAW_PAPERS_PATH = DATA_DIR / "raw_papers.json"
CLASSIFIED_PAPERS_PATH = DATA_DIR / "classified_papers.json"
SUMMARIZED_PAPERS_PATH = DATA_DIR / "summarized_papers.json"
PAPERS_STORE_PATH = DATA_DIR / "papers_store.json"
PAPERS_JSON_PATH = DATA_DIR / "papers.json"
PAPERS_CSV_PATH = DATA_DIR / "papers.csv"
PIPELINE_STATUS_PATH = DATA_DIR / "pipeline_status.json"
MARKDOWN_REPORT_PATH = DOCS_DIR / "index.md"


TABLE_FIELDS = [
    "arxiv_id",
    "base_arxiv_id",
    "version",
    "title",
    "authors",
    "published",
    "updated",
    "arxiv_url",
    "pdf_url",
    "arxiv_categories",
    "domain_keywords",
    "topic_keywords",
    "abstract_en",
    "abstract_zh",
    "summary_zh",
]


@dataclass(frozen=True)
class KeywordGroup:
    label: str
    aliases: list[str]


@dataclass(frozen=True)
class AppConfig:
    max_results: int
    overfetch_factor: int
    arxiv_num_retries: int
    arxiv_request_timeout: float
    arxiv_categories: list[str]
    domain_keywords: list[KeywordGroup]
    topic_keywords: list[KeywordGroup]
    gemini_model: str

    @property
    def arxiv_fetch_limit(self) -> int:
        return max(self.max_results * self.overfetch_factor, self.max_results)


def load_config() -> AppConfig:
    if load_dotenv is not None:
        load_dotenv(ROOT_DIR / ".env")
    return AppConfig(
        max_results=int(os.getenv("MAX_RESULTS", "100")),
        overfetch_factor=int(os.getenv("ARXIV_OVERFETCH_FACTOR", "4")),
        arxiv_num_retries=int(os.getenv("ARXIV_NUM_RETRIES", "1")),
        arxiv_request_timeout=float(os.getenv("ARXIV_REQUEST_TIMEOUT", "20")),
        arxiv_categories=["cs.CV", "cs.RO", "cs.AI", "cs.LG"],
        domain_keywords=[
            KeywordGroup(
                label="autonomous driving",
                aliases=[
                    "autonomous driving",
                    "self-driving",
                    "self driving",
                    "autonomous vehicle",
                    "autonomous vehicles",
                    "automated driving",
                    "driving automation",
                ],
            ),
            KeywordGroup(
                label="end-to-end",
                aliases=[
                    "end-to-end",
                    "end to end",
                    "end2end",
                    "e2e",
                ],
            ),
        ],
        topic_keywords=[
            KeywordGroup(
                label="VLM",
                aliases=[
                    "VLM",
                    "VLMs",
                    "vision-language model",
                    "vision-language models",
                    "vision language model",
                    "vision language models",
                    "large vision-language model",
                    "large vision-language models",
                    "large vision language model",
                    "large vision language models",
                    "LVLM",
                    "LVLMs",
                ],
            ),
            KeywordGroup(
                label="world model",
                aliases=[
                    "world model",
                    "world models",
                    "world-model",
                    "world-models",
                ],
            ),
            KeywordGroup(
                label="distillation",
                aliases=[
                    "distillation",
                    "distill",
                    "distilled",
                    "knowledge distillation",
                ],
            ),
            KeywordGroup(
                label="RL",
                aliases=[
                    "RL",
                    "reinforcement learning",
                    "reinforcement-learning",
                    "policy gradient",
                    "reinforcement fine-tuning",
                    "reinforcement finetuning",
                ],
            ),
        ],
        gemini_model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
    )
