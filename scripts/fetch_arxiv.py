from __future__ import annotations

import argparse
import sys
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


def build_query() -> str:
    config = load_config()
    categories = " OR ".join(f"cat:{category}" for category in config.arxiv_categories)
    domain = _query_groups_all(config.domain_keywords)
    topics = _query_groups_any(config.topic_keywords)
    return f"({categories}) AND ({domain}) AND ({topics})"


def _paper_id(entry_id: str) -> str:
    return entry_id.rstrip("/").split("/")[-1]


def fetch_papers() -> list[dict]:
    try:
        import arxiv
    except ImportError as exc:
        raise RuntimeError("Missing dependency: install requirements.txt before fetching arXiv papers.") from exc

    config = load_config()
    page_size = min(100, config.arxiv_fetch_limit)
    client = arxiv.Client(page_size=page_size, delay_seconds=3, num_retries=config.arxiv_num_retries)
    _set_request_timeout(client, config.arxiv_request_timeout)
    search = arxiv.Search(
        query=build_query(),
        max_results=config.arxiv_fetch_limit,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    papers_by_id: dict[str, dict] = {}
    print("start!")
    for result in client.results(search):
        print("processing ...")
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
    return papers[: config.max_results]


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch recent arXiv papers for autonomous driving topics.")
    parser.add_argument("--dry-run", action="store_true", help="Print the query instead of writing files.")
    args = parser.parse_args()

    if args.dry_run:
        print(build_query())
        return 0

    papers = fetch_papers()
    write_json(RAW_PAPERS_PATH, papers)
    print(f"Wrote {len(papers)} papers to {RAW_PAPERS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
