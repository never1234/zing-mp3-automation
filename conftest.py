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


@pytest.fixture(scope="session")
def driver(request):
    """
    Khởi động Appium driver theo platform được chọn
    Dùng chung cho toàn bộ test session
    """
    platform = request.config.getoption("--platform")
    os.environ["PLATFORM"] = platform  # Truyền vào BasePage

    appium_server = os.getenv("APPIUM_HOST", "http://localhost:4723")

    if platform == "android":
        options = UiAutomator2Options().load_capabilities(ANDROID_CAPS)
    else:
        options = XCUITestOptions().load_capabilities(IOS_CAPS)

    print(f"\n[START] Khoi dong {platform.upper()} driver...")

    driver = webdriver.Remote(command_executor=appium_server, options=options)
    # implicitly_wait(0) để tránh double-wait với explicit WebDriverWait
    driver.implicitly_wait(0)

    yield driver

    print(f"\n[STOP] Dong {platform.upper()} driver...")
    driver.quit()


def _navigate_to_home(driver):
    """Về màn hình Khám phá (Home tab) — dùng explicit wait thay vì sleep cứng"""
    try:
        by, value = AndroidHomeLocators.BOTTOM_NAV_HOME
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((by, value))
        ).click()
    except Exception:
        pass


@pytest.fixture(scope="function", autouse=True)
def reset_to_home(driver):
    """Điều hướng về màn hình Home (tab Khám phá) trước mỗi test"""
    _navigate_to_home(driver)
    yield


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, driver):
    """Tự động chụp màn hình khi test FAIL"""
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        test_name = request.node.name
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
