from pathlib import Path


def test_daily_workflow_fetches_recent_metadata_on_schedule():
    workflow = Path(".github/workflows/daily-report.yml").read_text(encoding="utf-8")

    assert "github.event_name == 'schedule'" in workflow
    assert "python scripts/update_paper_base.py --recent-days 7" in workflow


def test_manual_workflow_can_control_update_paper_base_step():
    workflow = Path(".github/workflows/daily-report.yml").read_text(encoding="utf-8")

    assert "run_update_paper_base:" in workflow
    assert "inputs.run_update_paper_base" in workflow
