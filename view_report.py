"""
Serve Allure report via HTTP server and export PDF using Chrome headless.
Run: python view_report.py
- Generate report to a TEMP folder moi moi lan -> khong bi lock boi Chrome
- Serve qua HTTP server -> xem duoc tren trinh duyet
- Xuat PDF bang Chrome headless
"""
import http.server
import threading
import subprocess
import socket
import time
import os
import sys
import tempfile
import webbrowser
from pathlib import Path
from datetime import datetime


BASE_DIR    = Path(__file__).parent.resolve()
RESULTS_DIR = BASE_DIR / "reports" / "allure-results"
PDF_DIR     = BASE_DIR / "reports" / "pdf"

CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
]


# ─────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────

def find_chrome():
    return next((p for p in CHROME_PATHS if os.path.exists(p)), None)


def find_free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def make_handler(directory: str):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)
        def log_message(self, *args):
            pass  # suppress access logs
    return Handler


def start_server(directory: str, port: int):
    server = http.server.HTTPServer(("127.0.0.1", port), make_handler(str(directory)))
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    return server


# ─────────────────────────────────────────
# Step 1: Generate report -> TEMP folder
# ─────────────────────────────────────────

def generate_allure_report() -> Path:
    print("[1/3] Generating Allure report...")

    # Dung tempfile.mkdtemp() -> moi lan tao folder moi, khong xung dot voi Chrome
    report_dir = Path(tempfile.mkdtemp(prefix="allure-report-"))
    print(f"      Output: {report_dir}")

    result = subprocess.run(
        ["allure", "generate", str(RESULTS_DIR), "-o", str(report_dir), "--clean"],
        capture_output=True, text=True, shell=True
    )
    if result.returncode != 0:
        print(f"[LOI] allure generate that bai:\n{result.stderr}")
        input("Nhan Enter de thoat...")
        sys.exit(1)

    print(f"[OK] Report HTML da tao.")
    return report_dir


# ─────────────────────────────────────────
# Step 2: Export PDF bang Chrome headless
# ─────────────────────────────────────────

def export_pdf(port: int):
    print("\n[2/3] Xuat PDF...")
    chrome = find_chrome()
    if not chrome:
        print("[CANH BAO] Khong tim thay Chrome. Bo qua PDF.")
        return

    PDF_DIR.mkdir(parents=True, exist_ok=True)
    ts       = datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_path = PDF_DIR / f"allure-report_{ts}.pdf"
    url      = f"http://127.0.0.1:{port}/index.html"

    print(f"      URL : {url}")
    print(f"      PDF : {pdf_path}")
    print("      Cho Chrome render (20 giay)...")

    # Dung user-data-dir rieng de tranh xung dot voi Chrome dang mo
    tmp_profile = Path(tempfile.mkdtemp(prefix="chrome-pdf-"))

    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-extensions",
        "--disable-dev-shm-usage",
        f"--user-data-dir={tmp_profile}",
        f"--print-to-pdf={pdf_path}",
        "--print-to-pdf-no-header",
        "--virtual-time-budget=20000",
        "--run-all-compositor-stages-before-draw",
        "--no-first-run",
        "--no-default-browser-check",
        url,
    ]

    try:
        subprocess.run(cmd, timeout=50, capture_output=True)
    except subprocess.TimeoutExpired:
        print("      [CANH BAO] Timeout nhung PDF co the da duoc tao.")

    if pdf_path.exists() and pdf_path.stat().st_size > 1000:
        print(f"[OK] PDF da luu: {pdf_path}")
        subprocess.Popen(["explorer", str(PDF_DIR)])
    else:
        print("[CANH BAO] PDF khong duoc tao hoac bi rong.")

    # Don dep profile tam
    try:
        import shutil
        shutil.rmtree(tmp_profile, ignore_errors=True)
    except Exception:
        pass


# ─────────────────────────────────────────
# Step 3: Mo trinh duyet qua HTTP
# ─────────────────────────────────────────

def open_browser(port: int):
    url = f"http://127.0.0.1:{port}/index.html"
    print(f"\n[3/3] Mo trinh duyet: {url}")
    webbrowser.open(url)
    return url


# ─────────────────────────────────────────
# Main
# ─────────────────────────────────────────

def main():
    print("=" * 50)
    print("  ALLURE REPORT - XEM VA LUU PDF")
    print(f"  Project: {BASE_DIR}")
    print("=" * 50 + "\n")

    # Kiem tra allure-results ton tai
    if not RESULTS_DIR.exists():
        print(f"[LOI] Khong tim thay: {RESULTS_DIR}")
        print("      Hay chay test truoc.")
        input("Nhan Enter de thoat...")
        sys.exit(1)

    result_files = list(RESULTS_DIR.glob("*-result.json"))
    if not result_files:
        print(f"[LOI] Khong co du lieu test trong {RESULTS_DIR}")
        print("      Hay chay test truoc.")
        input("Nhan Enter de thoat...")
        sys.exit(1)

    print(f"[OK] Tim thay {len(result_files)} test result(s).\n")

    # 1. Generate report -> temp folder (khong lien quan den folder cu)
    report_dir = generate_allure_report()

    # 2. Start HTTP server phuc vu static files
    port   = find_free_port()
    server = start_server(str(report_dir), port)
    time.sleep(1)  # cho server san sang

    # 3. Xuat PDF (dung cung port)
    export_pdf(port)

    # 4. Mo browser
    url = open_browser(port)

    print("\n" + "=" * 50)
    print("  Allure Report dang chay qua HTTP server")
    print(f"  URL: {url}")
    print("  Nhan Ctrl+C de thoat")
    print("=" * 50 + "\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] Dung server.")
        server.shutdown()


if __name__ == "__main__":
    main()
