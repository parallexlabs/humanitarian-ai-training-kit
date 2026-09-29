#!/usr/bin/env python3
"""Run axe-core accessibility audit on built HTML pages."""

from __future__ import annotations

import argparse
import json
import socket
import subprocess
import sys
import time
from pathlib import Path
from threading import Thread
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
REPORT = BUILD / "axe-report.json"
AXE_JS = Path(__file__).resolve().parent / "axe.min.js"


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def start_server(directory: Path, port: int) -> ThreadingHTTPServer:
    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(directory), **kwargs)

    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def audit_page(page, url: str, axe_js: str) -> dict:
    page.goto(url, wait_until="domcontentloaded")
    page.evaluate(axe_js)
    result = page.evaluate(
        """async () => await axe.run(document, {
            runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag22a', 'wcag22aa'] }
        })"""
    )
    violations = result.get("violations", [])
    return {
        "url": url,
        "violations": violations,
        "violation_count": len(violations),
        "passes": len(result.get("passes", [])),
    }


def run_audit(build_dir: Path = BUILD) -> dict:
    from playwright.sync_api import sync_playwright

    if not AXE_JS.exists():
        raise FileNotFoundError(f"Missing {AXE_JS}; download axe-core first")

    axe_js = AXE_JS.read_text(encoding="utf-8")
    html_files = sorted(
        p for p in build_dir.rglob("*.html")
        if "_pdf_tmp" not in p.parts and not (p.name == "index.html" and p.parent == build_dir)
    )

    port = free_port()
    server = start_server(build_dir, port)
    time.sleep(0.3)

    report: dict = {
        "pages": [],
        "total_violations": 0,
        "pages_with_violations": 0,
        "passed": True,
    }

    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            page = browser.new_page()
            for html_path in html_files:
                rel = html_path.relative_to(build_dir).as_posix()
                url = f"http://127.0.0.1:{port}/{rel}"
                entry = audit_page(page, url, axe_js)
                report["pages"].append(entry)
                if entry["violation_count"]:
                    report["pages_with_violations"] += 1
                    report["total_violations"] += entry["violation_count"]
                    report["passed"] = False
            browser.close()
    finally:
        server.shutdown()

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="axe-core WCAG 2.2 audit")
    parser.add_argument("--build-dir", type=Path, default=BUILD)
    args = parser.parse_args()
    if not args.build_dir.exists():
        print("Build directory missing; run scripts/build.py first", file=sys.stderr)
        return 1
    report = run_audit(args.build_dir)
    print(json.dumps({"total_violations": report["total_violations"], "passed": report["passed"]}, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
