from __future__ import annotations

import argparse
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from paper_app.config import KeywordGroup, RAW_PAPERS_PATH, load_config
from paper_app.storage import write_json


def _query_terms(keywords: list[str]) -> str:
    terms = []
    for keyword in keywords:
        escaped = keyword.replace('"', "")
        terms.append(f'ti:"{escaped}"')
        terms.append(f'abs:"{escaped}"')
    return " OR ".join(terms)


def _query_group(keyword_group: KeywordGroup) -> str:
    return f"({_query_terms(keyword_group.aliases)})"


def _query_groups_any(keyword_groups: list[KeywordGroup]) -> str:
    return " OR ".join(_query_group(keyword_group) for keyword_group in keyword_groups)


def _query_groups_all(keyword_groups: list[KeywordGroup]) -> str:
    return " AND ".join(_query_group(keyword_group) for keyword_group in keyword_groups)


def _set_request_timeout(client, timeout: float) -> None:
    original_get = client._session.get

    def get_with_timeout(url, **kwargs):
        kwargs.setdefault("timeout", timeout)
        return original_get(url, **kwargs)

    client._session.get = get_with_timeout


def _arxiv_date(value: datetime) -> str:
    return value.astimezone(timezone.utc).strftime("%Y%m%d%H%M")


def _recent_submitted_query(recent_days: int, now: datetime | None = None) -> str:
    if recent_days <= 0:
        raise ValueError("--recent-days must be greater than 0.")
    end = now or datetime.now(timezone.utc)
    start = end - timedelta(days=recent_days)
    return f"submittedDate:[{_arxiv_date(start)} TO {_arxiv_date(end)}]"


def build_query(recent_days: int | None = None, now: datetime | None = None) -> str:
    config = load_config()
    categories = " OR ".join(f"cat:{category}" for category in config.arxiv_categories)
    domain = _query_groups_all(config.domain_keywords)
    topics = _query_groups_any(config.topic_keywords)
    query = f"({categories}) AND ({domain}) AND ({topics})"
    if recent_days is not None:
        query = f"({query}) AND {_recent_submitted_query(recent_days, now)}"
    return query


def _paper_id(entry_id: str) -> str:
    return entry_id.rstrip("/").split("/")[-1]


def _error_summary(exc: Exception) -> str:
    return f"{type(exc).__name__}: {exc}"


def _fetch_papers_once(arxiv, config, recent_days: int | None = None) -> list[dict]:
    fetch_limit = config.arxiv_recent_fetch_limit if recent_days is not None else config.arxiv_fetch_limit
    page_size = min(100, fetch_limit)
    client = arxiv.Client(page_size=page_size, delay_seconds=3, num_retries=config.arxiv_num_retries)
    _set_request_timeout(client, config.arxiv_request_timeout)
    search = arxiv.Search(
        query=build_query(recent_days=recent_days),
        max_results=fetch_limit,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    papers_by_id: dict[str, dict] = {}
    print(
        f"Fetching arXiv papers: max_results={config.max_results}, "
        f"fetch_limit={fetch_limit}, recent_days={recent_days or 'none'}, "
        f"timeout={config.arxiv_request_timeout:g}s",
        flush=True,
    )
    for index, result in enumerate(client.results(search), start=1):
        if index == 1 or index % 25 == 0:
            print(f"Received {index} arXiv results...", flush=True)
        paper = {
            "arxiv_id": _paper_id(result.entry_id),
            "title": " ".join(result.title.split()),
            "authors": [author.name for author in result.authors],
            "published": result.published.isoformat(),
            "updated": result.updated.isoformat(),
            "arxiv_url": result.entry_id,
            "pdf_url": result.pdf_url,
            "arxiv_categories": list(result.categories),
            "abstract_en": " ".join(result.summary.split()),
            "abstract_zh": "",
            "summary_zh": "",
        }
        papers_by_id[paper["arxiv_id"]] = paper

    papers = sorted(
        papers_by_id.values(),
        key=lambda item: item.get("published", ""),
        reverse=True,
    )
    if recent_days is not None:
        return papers
    return papers[: config.max_results]


def fetch_papers(recent_days: int | None = None) -> list[dict]:
    try:
        import arxiv
    except ImportError as exc:
        raise RuntimeError("Missing dependency: install requirements.txt before fetching arXiv papers.") from exc

    config = load_config()
    max_attempts = max(1, config.arxiv_num_retries + 1)
    last_exc: Exception | None = None
    for attempt in range(1, max_attempts + 1):
        try:
            return _fetch_papers_once(arxiv, config, recent_days=recent_days)
        except Exception as exc:
            last_exc = exc
            if attempt >= max_attempts:
                break
            wait_seconds = 15 * attempt
            print(
                f"arXiv fetch attempt {attempt}/{max_attempts} failed: {_error_summary(exc)}. "
                f"Waiting {wait_seconds}s before retry.",
                flush=True,
            )
            time.sleep(wait_seconds)
    reason = _error_summary(last_exc) if last_exc is not None else "unknown error"
    raise RuntimeError(f"arXiv fetch failed after {max_attempts} attempts. Last error: {reason}") from last_exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch recent arXiv papers for autonomous driving topics.")
    parser.add_argument("--dry-run", action="store_true", help="Print the query instead of writing files.")
    parser.add_argument("--recent-days", type=int, default=None, help="Limit query to papers submitted in the last N days.")
    args = parser.parse_args()

    if args.dry_run:
        print(build_query(recent_days=args.recent_days))
        return 0

    papers = fetch_papers(recent_days=args.recent_days)
    write_json(RAW_PAPERS_PATH, papers)
    print(f"Wrote {len(papers)} papers to {RAW_PAPERS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
