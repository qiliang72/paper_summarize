from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from paper_app.config import PAPERS_CSV_PATH, PAPERS_JSON_PATH, SUMMARIZED_PAPERS_PATH, TABLE_FIELDS
from paper_app.storage import ensure_parent, read_json, write_json


def _normalize_paper(paper: dict[str, Any]) -> dict[str, Any]:
    normalized = {field: paper.get(field, "" if field not in {"authors", "arxiv_categories", "domain_keywords", "topic_keywords"} else []) for field in TABLE_FIELDS}
    for field in ["authors", "arxiv_categories", "domain_keywords", "topic_keywords"]:
        if isinstance(normalized[field], str):
            normalized[field] = [item.strip() for item in normalized[field].split(";") if item.strip()]
    return normalized


def write_csv(path: Path, papers: list[dict[str, Any]]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=TABLE_FIELDS)
        writer.writeheader()
        for paper in papers:
            row = dict(paper)
            for field in ["authors", "arxiv_categories", "domain_keywords", "topic_keywords"]:
                row[field] = "; ".join(row.get(field, []))
            writer.writerow(row)


def export_table(papers: list[dict[str, Any]], json_path: Path = PAPERS_JSON_PATH, csv_path: Path = PAPERS_CSV_PATH) -> list[dict[str, Any]]:
    normalized = [_normalize_paper(paper) for paper in papers]
    write_json(json_path, normalized)
    write_csv(csv_path, normalized)
    return normalized


def main() -> int:
    parser = argparse.ArgumentParser(description="Export summarized paper records to JSON and CSV tables.")
    parser.add_argument("--input", type=Path, default=SUMMARIZED_PAPERS_PATH)
    parser.add_argument("--json-output", type=Path, default=PAPERS_JSON_PATH)
    parser.add_argument("--csv-output", type=Path, default=PAPERS_CSV_PATH)
    args = parser.parse_args()

    papers = read_json(args.input, [])
    exported = export_table(papers, json_path=args.json_output, csv_path=args.csv_output)
    print(f"Wrote {len(exported)} papers to {args.json_output} and {args.csv_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

