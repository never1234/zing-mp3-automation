import os
from dotenv import load_dotenv

load_dotenv()

ANDROID_CAPS = {
    "platformName":        "Android",
    "deviceName":          os.getenv("ANDROID_DEVICE", "RFCX309KX8Z"),
    "platformVersion":     os.getenv("ANDROID_PLATFORM_VERSION", "16"),
    "appPackage":          "com.zing.mp3",
    "appActivity":         ".ui.activity.SplashActivity",
    "automationName":      "UiAutomator2",
    "noReset":             True,       # giữ dữ liệu giữa các lần chạy
    "newCommandTimeout":   120,
    "autoGrantPermissions": True       # tự động cấp quyền app
}
