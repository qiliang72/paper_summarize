from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from paper_app.config import PAPERS_STORE_PATH
from paper_app.paper_store import merge_new_papers, read_paper_store, write_paper_store
from scripts.classify_keywords import classify_papers
from scripts.fetch_arxiv import build_query, fetch_papers


def update_paper_base(store_path: Path = PAPERS_STORE_PATH) -> tuple[list[dict], list[dict]]:
    existing = read_paper_store(store_path)
    fetched = fetch_papers()
    classified = classify_papers(fetched)
    merged, added = merge_new_papers(existing, classified)
    write_paper_store(merged, store_path)
    return merged, added


def main() -> int:
    parser = argparse.ArgumentParser(description="Manually fetch arXiv papers and append new paper versions to the local store.")
    parser.add_argument("--store", type=Path, default=PAPERS_STORE_PATH)
    parser.add_argument("--dry-run", action="store_true", help="Print the arXiv query without fetching or writing files.")
    args = parser.parse_args()

    if args.dry_run:
        print(build_query())
        print(f"Store path: {args.store}")
        return 0

    merged, added = update_paper_base(args.store)
    print(f"Added {len(added)} new paper versions. Store now has {len(merged)} records at {args.store}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
