from __future__ import annotations

import argparse
import html
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from paper_app.config import MARKDOWN_REPORT_PATH, PAPERS_CSV_PATH, PAPERS_JSON_PATH, PAPERS_STORE_PATH
from paper_app.paper_store import latest_papers, latest_papers_with_versions, read_paper_store
from paper_app.storage import ensure_parent
from scripts.export_table import export_table


def _escape(value: Any) -> str:
    return html.escape(str(value or ""), quote=True)


def _list_text(value: Any) -> str:
    if not value:
        return ""
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return str(value)


def _date_text(value: Any) -> str:
    if not value:
        return ""
    return str(value).split("T", 1)[0]


def _version_label(paper: dict[str, Any]) -> str:
    version = paper.get("version")
    return f"v{version}" if isinstance(version, int) else str(paper.get("arxiv_id", ""))


def _links_cell(paper: dict[str, Any]) -> str:
    links = [
        f'<a href="{_escape(paper.get("arxiv_url"))}">{_escape(paper.get("arxiv_id"))}</a>',
        f'<a href="{_escape(paper.get("pdf_url"))}">PDF</a>',
    ]
    old_links = [
        f'<a href="{_escape(old.get("arxiv_url"))}">{_escape(_version_label(old))}</a>'
        for old in paper.get("older_versions", [])
        if old.get("arxiv_url")
    ]
    old_versions = f'<div class="old-versions">旧版：{", ".join(old_links)}</div>' if old_links else ""
    return (
        f'<div>{_date_text(paper.get("published"))}</div>'
        f'<div>{_date_text(paper.get("updated"))}</div>'
        f'<div>{" / ".join(links)}</div>'
        f"{old_versions}"
    )


def _abstract_cell(paper: dict[str, Any]) -> str:
    abstract = paper.get("abstract_zh") or paper.get("abstract_en") or ""
    if not abstract:
        return ""
    label = "中文摘要" if paper.get("abstract_zh") else "Abstract"
    return f"<strong>{label}</strong><br>{_escape(abstract)}"


def _summary_cell(paper: dict[str, Any]) -> str:
    summary = paper.get("summary_zh", "")
    if not summary:
        return ""
    return _escape(summary)


def render_markdown(papers: list[dict[str, Any]]) -> str:
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    rows = []
    for index, paper in enumerate(papers, start=1):
        title = (
            f'<strong>{index}. {_escape(paper.get("title", "Untitled"))}</strong>'
            f'<br><span>{_escape(_list_text(paper.get("authors")))}</span>'
        )
        keywords = _escape(_list_text(paper.get("topic_keywords", [])))
        categories = _escape(_list_text(paper.get("arxiv_categories")))
        rows.append(
            "    <tr>\n"
            f'      <td style="width: 23%; vertical-align: top;">{title}</td>\n'
            f'      <td style="width: 13%; vertical-align: top;">{_links_cell(paper)}<div>{categories}</div></td>\n'
            f'      <td style="width: 10%; vertical-align: top;">{keywords}</td>\n'
            f'      <td style="width: 34%; vertical-align: top;">{_abstract_cell(paper)}</td>\n'
            f'      <td style="width: 20%; vertical-align: top;">{_summary_cell(paper)}</td>\n'
            "    </tr>"
        )

    return (
        "# arXiv 自动驾驶论文\n\n"
        f"Generated: {generated_at}\n\n"
        f"当前展示 {len(papers)} 篇论文的最新版本。旧版本只保留 arXiv 链接。\n\n"
        '<table style="table-layout: fixed; width: 100%;">\n'
        "  <colgroup>\n"
        '    <col style="width: 23%;">\n'
        '    <col style="width: 13%;">\n'
        '    <col style="width: 10%;">\n'
        '    <col style="width: 34%;">\n'
        '    <col style="width: 20%;">\n'
        "  </colgroup>\n"
        "  <thead>\n"
        "    <tr>\n"
        "      <th>标题 / 作者</th>\n"
        "      <th>信息</th>\n"
        "      <th>关键词</th>\n"
        "      <th>摘要</th>\n"
        "      <th>简短总结</th>\n"
        "    </tr>\n"
        "  </thead>\n"
        "  <tbody>\n"
        + "\n".join(rows)
        + "\n  </tbody>\n"
        "</table>\n"
    )


def export_markdown(
    store_path: Path = PAPERS_STORE_PATH,
    markdown_path: Path = MARKDOWN_REPORT_PATH,
    json_path: Path = PAPERS_JSON_PATH,
    csv_path: Path = PAPERS_CSV_PATH,
) -> list[dict[str, Any]]:
    store = read_paper_store(store_path)
    latest_for_tables = latest_papers(store)
    latest_for_markdown = latest_papers_with_versions(store)
    export_table(latest_for_tables, json_path=json_path, csv_path=csv_path)
    ensure_parent(markdown_path)
    markdown_path.write_text(render_markdown(latest_for_markdown), encoding="utf-8")
    return latest_for_tables


def main() -> int:
    parser = argparse.ArgumentParser(description="Export latest paper versions to JSON, CSV, and a Markdown report.")
    parser.add_argument("--store", type=Path, default=PAPERS_STORE_PATH)
    parser.add_argument("--markdown-output", type=Path, default=MARKDOWN_REPORT_PATH)
    parser.add_argument("--json-output", type=Path, default=PAPERS_JSON_PATH)
    parser.add_argument("--csv-output", type=Path, default=PAPERS_CSV_PATH)
    args = parser.parse_args()

    exported = export_markdown(args.store, args.markdown_output, args.json_output, args.csv_output)
    print(f"Wrote {len(exported)} latest papers to {args.markdown_output}, {args.json_output}, and {args.csv_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
