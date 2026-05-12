from __future__ import annotations

import subprocess
import sys
import threading
from pathlib import Path

from flask import Flask, jsonify, render_template

from paper_app.config import PAPERS_JSON_PATH, PIPELINE_STATUS_PATH, ROOT_DIR
from paper_app.storage import read_json, utc_now_iso, write_json


app = Flask(__name__)
_pipeline_lock = threading.Lock()
_pipeline_process: subprocess.Popen | None = None


def _default_status() -> dict:
    return {"status": "idle", "message": "尚未运行。", "updated_at": ""}


def _watch_process(process: subprocess.Popen) -> None:
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        write_json(PIPELINE_STATUS_PATH, {"status": "success", "message": "更新完成。", "updated_at": utc_now_iso()})
    else:
        message = stderr.strip() or stdout.strip() or "更新失败。"
        write_json(PIPELINE_STATUS_PATH, {"status": "error", "message": message[-2000:], "updated_at": utc_now_iso()})


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/papers")
def papers():
    return jsonify(read_json(PAPERS_JSON_PATH, []))


@app.get("/api/status")
def status():
    return jsonify(read_json(PIPELINE_STATUS_PATH, _default_status()))


@app.post("/api/run")
def run_pipeline():
    global _pipeline_process
    with _pipeline_lock:
        if _pipeline_process is not None and _pipeline_process.poll() is None:
            return jsonify({"status": "running", "message": "已有更新任务正在运行。"}), 409

        write_json(PIPELINE_STATUS_PATH, {"status": "running", "message": "正在启动更新任务...", "updated_at": utc_now_iso()})
        _pipeline_process = subprocess.Popen(
            [sys.executable, str(ROOT_DIR / "scripts" / "run_pipeline.py")],
            cwd=ROOT_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        threading.Thread(target=_watch_process, args=(_pipeline_process,), daemon=True).start()
    return jsonify({"status": "running", "message": "更新任务已启动。"})


if __name__ == "__main__":
    app.run(debug=True)
