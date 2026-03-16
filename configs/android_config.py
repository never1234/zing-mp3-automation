import os
from dotenv import load_dotenv

load_dotenv()

ANDROID_CAPS = {
    "platformName":        "Android",
    "deviceName":          os.getenv("ANDROID_DEVICE", "RFCX309KX8Z"),
    "platformVersion":     os.getenv("ANDROID_PLATFORM_VERSION", "16"),
    "appPackage":          "com.zing.mp3",
    "appActivity":         "com.zing.mp3.ui.activity.MainScreenActivity",
    "automationName":      "UiAutomator2",
    "noReset":             True,
    "newCommandTimeout":   60,
    "autoGrantPermissions": True,

    # ── Performance: giảm thời gian khởi động ────────────────────────────────
    "skipServerInstallation":   True,   # không cài lại Appium server mỗi lần
    "skipDeviceInitialization": True,   # không khởi tạo lại device
    "skipUnlock":               True,   # không unlock màn hình
    "disableWindowAnimation":   True,   # tắt animation → thao tác nhanh hơn
}
