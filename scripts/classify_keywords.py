from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from paper_app.config import CLASSIFIED_PAPERS_PATH, RAW_PAPERS_PATH, load_config
from paper_app.keyword_utils import find_keyword_matches
from paper_app.storage import read_json, write_json


def classify_papers(papers: list[dict]) -> list[dict]:
    config = load_config()
    classified = []
    for paper in papers:
        text = f"{paper.get('title', '')} {paper.get('abstract_en', '')}"
        updated = dict(paper)
        updated["domain_keywords"] = find_keyword_matches(text, config.domain_keywords)
        updated["topic_keywords"] = find_keyword_matches(text, config.topic_keywords)
        classified.append(updated)
    return classified


def main() -> int:
    parser = argparse.ArgumentParser(description="Classify papers by configured domain and topic keywords.")
    parser.add_argument("--input", type=Path, default=RAW_PAPERS_PATH)
    parser.add_argument("--output", type=Path, default=CLASSIFIED_PAPERS_PATH)
    args = parser.parse_args()

    papers = read_json(args.input, [])
    classified = classify_papers(papers)
    write_json(args.output, classified)
    print(f"Wrote {len(classified)} classified papers to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

