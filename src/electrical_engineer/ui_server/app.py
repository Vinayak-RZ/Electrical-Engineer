"""Persistent UI HTTP server. Bind 127.0.0.1 only."""

from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles

BIND_HOST = "127.0.0.1"
BIND_PORT = 8765
_PNG = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
    b"\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\xf8\x0f\x00"
    b"\x00\x01\x01\x00\x00\x05\x18\xd8N\x00\x00\x00\x00IEND\xaeB`\x82"
)
_SVG = "<svg xmlns='http://www.w3.org/2000/svg' width='1' height='1'></svg>"


def create_app(root: Path | None = None) -> FastAPI:
    app = FastAPI()
    runs = (root or Path.cwd()) / "runs"

    @app.get("/api/health")
    def health() -> dict:
        return {"bind": BIND_HOST, "ok": True}

    @app.get("/api/runs")
    def list_runs() -> dict:
        items = []
        if runs.is_dir():
            items = sorted(p.name for p in runs.iterdir() if p.is_dir())
        return {"runs": items}

    @app.get("/api/runs/{run_id}")
    def run_detail(run_id: str) -> dict:
        summary = runs / run_id / "summary.json"
        if not summary.is_file():
            return JSONResponse({"error": "missing"}, status_code=404)
        return {"id": run_id, "summary": summary.read_text()}

    @app.get("/api/runs/{run_id}/artifact.svg")
    def artifact_svg(run_id: str) -> Response:
        path = runs / run_id / "artifact.svg"
        body = path.read_text() if path.is_file() else _SVG
        return Response(body, media_type="image/svg+xml")

    @app.get("/api/runs/{run_id}/artifact.png")
    def artifact_png(run_id: str) -> Response:
        path = runs / run_id / "artifact.png"
        body = path.read_bytes() if path.is_file() else _PNG
        return Response(body, media_type="image/png")

    @app.post("/api/runs/{run_id}/confirm")
    def confirm(run_id: str) -> dict:
        d = runs / run_id
        d.mkdir(parents=True, exist_ok=True)
        (d / "confirmed.json").write_text('{"confirmed": true, "simulate": false}')
        return {"id": run_id, "confirmed": True, "simulate": False}

    ui_dist = Path(__file__).resolve().parents[3] / "ui" / "dist"
    index = ui_dist / "index.html"
    if index.is_file():
        app.mount("/assets", StaticFiles(directory=ui_dist / "assets"), name="assets")

        @app.get("/")
        def spa() -> FileResponse:
            return FileResponse(index)

    return app


def bind_host() -> str:
    return BIND_HOST


def should_open_browser() -> bool:
    return os.environ.get("EE_NO_BROWSER", "") not in {"1", "true", "TRUE"}
