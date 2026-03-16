import os
import time
import pytest
from appium import webdriver
from dotenv import load_dotenv
from configs.android_config import ANDROID_CAPS
from configs.ios_config import IOS_CAPS
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.android_locators import AndroidHomeLocators

load_dotenv()


def pytest_addoption(parser):
    """Thêm option --platform khi chạy pytest"""
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        choices=["android", "ios"],
        help="Platform cần chạy test: android | ios"
    )

def go_to_home(driver):
    """Về Home nhanh hơn — nhấn thẳng tab thay vì back nhiều lần"""
    try:
        home_tab = driver.find_element("id", "com.zing.mp3:id/nav_home")
        if home_tab.is_displayed():
            home_tab.click()
            time.sleep(0.5)  # giảm từ 1s → 0.5s
    except:
        pass

@pytest.fixture(scope="session")
def driver(request):
    """
    Khởi động Appium driver theo platform được chọn
    Dùng chung cho toàn bộ test session
    """
    platform = request.config.getoption("--platform")
    os.environ["PLATFORM"] = platform  # Truyền vào BasePage

    appium_server = os.getenv("APPIUM_HOST", "http://localhost:4723")

    # Chuyển đổi Dictionary Capabilities sang Options Object để tương thích Selenium 4
    if platform == "android":
        options = UiAutomator2Options().load_capabilities(ANDROID_CAPS)
    else:
        options = XCUITestOptions().load_capabilities(IOS_CAPS)

    print(f"\n[START] Khoi dong {platform.upper()} driver...")

    # Thay thế desired_capabilities bằng options
    driver = webdriver.Remote(command_executor=appium_server, options=options)
    driver.implicitly_wait(10)
    driver.activate_app("com.zing.mp3")

    yield driver  # Chạy test session

    print(f"\n[STOP] Dong {platform.upper()} driver...")
    driver.quit()


def _navigate_to_home(driver):
    """Bring app to foreground and navigate to Khám phá home tab"""
    try:
        driver.activate_app("com.zing.mp3")
        # Đợi bottom nav hiển thị (xử lý cả SplashActivity) thay vì sleep cố định
        by, value = AndroidHomeLocators.BOTTOM_NAV_HOME
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((by, value))).click()
        time.sleep(0.5)
    except Exception as e:
        print(f"\n[WARN] _navigate_to_home failed: {e}")


@pytest.fixture(scope="function", autouse=True)
def reset_to_home(driver):
    """Điều hướng về màn hình Home (tab Khám phá) trước mỗi test"""
    _navigate_to_home(driver)
    yield


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, driver):
    """Tự động chụp màn hình khi test FAIL"""
    yield
    # Kiểm tra nếu test case bị fail
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        test_name = request.node.name
        # Tạo thư mục nếu chưa tồn tại
        screenshot_dir = "reports/screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        path = f"{screenshot_dir}/{test_name}.png"
        driver.save_screenshot(path)
        print(f"\n[SCREENSHOT] Da luu tai: {path}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook để lấy kết quả test cho fixture screenshot_on_failure"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    ANDROID_CAPS = {
        "platformName": "Android",
        "deviceName": os.getenv("ANDROID_DEVICE", "RFCX309KX8Z"),
        "appPackage": "com.zing.mp3",
        "appActivity": "com.zing.mp3.ui.activity.MainScreenActivity",
        "automationName": "UiAutomator2",
        "noReset": True,
        "newCommandTimeout": 120,
        "autoGrantPermissions": True,

        # ── THÊM 4 DÒNG NÀY — giảm thời gian START ──────
        "skipServerInstallation": True,  # không cài lại server mỗi lần
        "skipDeviceInitialization": True,  # không khởi tạo device lại
        "skipUnlock": True,  # không unlock màn hình
        "disableWindowAnimation": True,  # tắt animation trong Appium
        # ─────────────────────────────────────────────────
    }