"""
Generate PDF from Allure static report via local HTTP server + Chrome headless.
"""
import http.server
import threading
import subprocess
import time
import sys
import os
import socket
from pathlib import Path


def find_free_port():
    with socket.socket() as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def start_http_server(directory: str, port: int):
    os.chdir(directory)
    handler = http.server.SimpleHTTPRequestHandler
    handler.log_message = lambda *a: None  # suppress logs
    server = http.server.HTTPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def generate_pdf(report_dir: str, pdf_path: str) -> bool:
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    ]
    chrome = next((p for p in chrome_paths if os.path.exists(p)), None)
    if not chrome:
        print("[LOI] Khong tim thay Chrome.")
        return False

    port = find_free_port()
    abs_report_dir = os.path.abspath(report_dir)
    abs_pdf_path = os.path.abspath(pdf_path)

    print(f"   Khoi dong HTTP server port {port}...")
    server = start_http_server(abs_report_dir, port)
    time.sleep(1)

    url = f"http://127.0.0.1:{port}/index.html"
    print(f"   Chrome headless -> {url}")
    print(f"   Dang xuat PDF (cho 12 giay)...")

    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-extensions",
        "--disable-dev-shm-usage",
        f"--print-to-pdf={abs_pdf_path}",
        "--print-to-pdf-no-header",
        "--virtual-time-budget=12000",
        "--run-all-compositor-stages-before-draw",
        url,
    ]

    try:
        subprocess.run(cmd, timeout=30, capture_output=True)
    except subprocess.TimeoutExpired:
        print("   [CANH BAO] Chrome qua thoi gian cho, PDF co the bi thieu trang.")
    finally:
        server.shutdown()

    return os.path.exists(abs_pdf_path)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_pdf.py <report_dir> <pdf_path>")
        sys.exit(1)

    report_dir = sys.argv[1]
    pdf_path = sys.argv[2]

    success = generate_pdf(report_dir, pdf_path)
    sys.exit(0 if success else 1)
