from __future__ import annotations

import argparse
import subprocess
import sys
import traceback
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from paper_app.config import DATA_DIR, PIPELINE_STATUS_PATH
from paper_app.storage import utc_now_iso, write_json


def _set_status(status: str, message: str = "") -> None:
    write_json(
        PIPELINE_STATUS_PATH,
        {
            "status": status,
            "message": message,
            "updated_at": utc_now_iso(),
        },
    )


def _run_step(script_name: str, extra_args: list[str] | None = None) -> None:
    command = [sys.executable, str(ROOT_DIR / "scripts" / script_name)]
    if extra_args:
        command.extend(extra_args)
    subprocess.run(command, cwd=ROOT_DIR, check=True)


def run_pipeline(offline: bool = False) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    _set_status("running", "Fetching arXiv papers...")
    _run_step("fetch_arxiv.py")
    _set_status("running", "Classifying keywords...")
    _run_step("classify_keywords.py")
    _set_status("running", "Summarizing abstracts...")
    summarize_args = ["--offline"] if offline else []
    _run_step("summarize_gemini.py", summarize_args)
    _set_status("running", "Exporting local tables...")
    _run_step("export_table.py")
    _set_status("success", "Pipeline completed.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the full arXiv paper pipeline.")
    parser.add_argument("--offline", action="store_true", help="Skip Gemini calls and use fallback summaries.")
    args = parser.parse_args()

    try:
        run_pipeline(offline=args.offline)
    except Exception as exc:
        _set_status("error", f"{exc}\n{traceback.format_exc(limit=2)}")
        raise
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
