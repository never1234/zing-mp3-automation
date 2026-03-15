import os
from dotenv import load_dotenv

load_dotenv()

IOS_CAPS = {
    "platformName":    "iOS",
    "deviceName":      os.getenv("IOS_DEVICE", "iPhone 15"),
    "platformVersion": os.getenv("IOS_PLATFORM_VERSION", "17.0"),
    "udid":            os.getenv("IOS_UDID", ""),     # lấy từ Xcode hoặc: xcrun xctrace list devices
    "bundleId":        "com.zing.mp3",
    "automationName":  "XCUITest",
    "noReset":         True,
    "newCommandTimeout": 60,
    "wdaLaunchTimeout": 120000        # thời gian khởi động WDA (iOS cần lâu hơn)
}
