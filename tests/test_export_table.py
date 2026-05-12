from pathlib import Path

from scripts.export_table import export_table


def test_export_table_writes_json_and_csv(tmp_path: Path):
    json_path = tmp_path / "papers.json"
    csv_path = tmp_path / "papers.csv"
    papers = [
        {
            "arxiv_id": "1234.5678",
            "title": "Test Paper",
            "authors": ["A", "B"],
            "published": "2026-01-01T00:00:00+00:00",
            "arxiv_categories": ["cs.CV"],
            "domain_keywords": ["autonomous driving"],
            "topic_keywords": ["VLM"],
        }
    ]

    exported = export_table(papers, json_path=json_path, csv_path=csv_path)

    assert exported[0]["authors"] == ["A", "B"]
    assert json_path.exists()
    assert csv_path.exists()
    assert "A; B" in csv_path.read_text(encoding="utf-8-sig")

