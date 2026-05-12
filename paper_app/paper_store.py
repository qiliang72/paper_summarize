from __future__ import annotations

import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from paper_app.config import PAPERS_JSON_PATH, PAPERS_STORE_PATH, SUMMARIZED_PAPERS_PATH
from paper_app.storage import read_json, write_json


VERSION_RE = re.compile(r"^(?P<base>.+?)v(?P<version>\d+)$")


def split_arxiv_id(arxiv_id: str) -> tuple[str, int | None]:
    match = VERSION_RE.match(str(arxiv_id).strip())
    if not match:
        return str(arxiv_id).strip(), None
    return match.group("base"), int(match.group("version"))


def normalize_paper_record(paper: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(paper)
    arxiv_id = str(normalized.get("arxiv_id", "")).strip()
    base_arxiv_id, version = split_arxiv_id(arxiv_id)
    normalized["arxiv_id"] = arxiv_id
    normalized["base_arxiv_id"] = normalized.get("base_arxiv_id") or base_arxiv_id
    normalized["version"] = normalized.get("version") if normalized.get("version") is not None else version
    normalized.setdefault("authors", [])
    normalized.setdefault("arxiv_categories", [])
    normalized.setdefault("domain_keywords", [])
    normalized.setdefault("topic_keywords", [])
    normalized.setdefault("abstract_en", "")
    normalized.setdefault("abstract_zh", "")
    normalized.setdefault("summary_zh", "")
    return normalized


def _date_sort_value(value: Any) -> float:
    if not value:
        return 0.0
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).timestamp()
    except ValueError:
        return 0.0


def paper_sort_key(paper: dict[str, Any]) -> tuple[float, int, str]:
    version = paper.get("version")
    version_value = version if isinstance(version, int) else -1
    return (_date_sort_value(paper.get("published")), version_value, str(paper.get("arxiv_id", "")))


def latest_sort_key(paper: dict[str, Any]) -> tuple[int, float, str]:
    version = paper.get("version")
    if isinstance(version, int):
        return (version, _date_sort_value(paper.get("updated")), str(paper.get("arxiv_id", "")))
    return (-1, _date_sort_value(paper.get("updated")), str(paper.get("arxiv_id", "")))


def merge_new_papers(existing: list[dict[str, Any]], incoming: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    merged = [normalize_paper_record(paper) for paper in existing]
    seen_ids = {paper.get("arxiv_id") for paper in merged}
    added: list[dict[str, Any]] = []

    for paper in incoming:
        normalized = normalize_paper_record(paper)
        if normalized.get("arxiv_id") in seen_ids:
            continue
        merged.append(normalized)
        added.append(normalized)
        seen_ids.add(normalized.get("arxiv_id"))

    merged.sort(key=paper_sort_key, reverse=True)
    return merged, added


def latest_papers_with_versions(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for paper in papers:
        normalized = normalize_paper_record(paper)
        groups[str(normalized.get("base_arxiv_id", normalized.get("arxiv_id", "")))].append(normalized)

    latest: list[dict[str, Any]] = []
    for versions in groups.values():
        newest = max(versions, key=latest_sort_key)
        older = [paper for paper in versions if paper.get("arxiv_id") != newest.get("arxiv_id")]
        older.sort(key=latest_sort_key, reverse=True)
        with_versions = dict(newest)
        with_versions["older_versions"] = older
        latest.append(with_versions)

    latest.sort(key=paper_sort_key, reverse=True)
    return latest


def latest_papers(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {key: value for key, value in paper.items() if key != "older_versions"}
        for paper in latest_papers_with_versions(papers)
    ]


def read_paper_store(path: Path = PAPERS_STORE_PATH) -> list[dict[str, Any]]:
    if path.exists():
        return [normalize_paper_record(paper) for paper in read_json(path, [])]
    for legacy_path in [SUMMARIZED_PAPERS_PATH, PAPERS_JSON_PATH]:
        if legacy_path.exists():
            return [normalize_paper_record(paper) for paper in read_json(legacy_path, [])]
    return []


def write_paper_store(papers: list[dict[str, Any]], path: Path = PAPERS_STORE_PATH) -> None:
    write_json(path, [normalize_paper_record(paper) for paper in papers])
