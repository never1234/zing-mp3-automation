import os
from dotenv import load_dotenv

load_dotenv()

WEB_CONFIG = {
    "base_url":  "https://zingmp3.vn",
    "browser":   os.getenv("BROWSER", "chrome"),   # chrome | firefox | edge
    "headless":  os.getenv("HEADLESS", "false").lower() == "true",
    "timeout":   10
}
