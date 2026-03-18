import os
import subprocess
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
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        choices=["android", "ios"],
        help="Platform cần chạy test: android | ios"
    )


def _cleanup_uiautomator2():
    """Kill UiAutomator2 server còn sót — tránh session conflict lần chạy sau"""
    for pkg in ("io.appium.uiautomator2.server", "io.appium.uiautomator2.server.test"):
        try:
            subprocess.run(["adb", "shell", "am", "force-stop", pkg],
                           timeout=5, capture_output=True)
        except Exception:
            pass


@pytest.fixture(scope="session")
def driver(request):
    platform = request.config.getoption("--platform")
    os.environ["PLATFORM"] = platform

    appium_server = os.getenv("APPIUM_HOST", "http://localhost:4723")
    options = UiAutomator2Options().load_capabilities(ANDROID_CAPS) \
        if platform == "android" else XCUITestOptions().load_capabilities(IOS_CAPS)

    # Dọn UiAutomator2 cũ trước khi tạo session — bắt buộc sau khi server bị crash
    if platform == "android":
        _cleanup_uiautomator2()

    print(f"\n[START] Khoi dong {platform.upper()} driver...")
    drv = webdriver.Remote(command_executor=appium_server, options=options)
    drv.implicitly_wait(0)  # tắt implicit wait — tránh double-wait với WebDriverWait

    yield drv

    print(f"\n[STOP] Dong {platform.upper()} driver...")
    try:
        drv.quit()
    except Exception:
        pass
    if platform == "android":
        _cleanup_uiautomator2()


def _navigate_to_home(driver):
    """Về tab Khám phá: activate app → minimize player → dismiss overlays → navigate"""
    from pages.base_page import BasePage
    from locators.android_locators import AndroidPlayerLocators

    page = BasePage(driver)

    # 1. Đảm bảo app đang ở foreground trước khi làm bất cứ điều gì
    try:
        if driver.current_package != "com.zing.mp3":
            driver.activate_app("com.zing.mp3")
    except Exception:
        pass

    # 2. Minimize full Player nếu đang mở (che khuất bottom nav)
    # Dùng PLAY_PAUSE_BTN (com.zing.mp3:id/btnPlay) — chỉ tồn tại trên full Player,
    # khác với mini player dùng btnPlayPause
    if page.is_visible(AndroidPlayerLocators.PLAY_PAUSE_BTN):
        try:
            page.minimize_player()
        except Exception:
            pass

    # 3. Dismiss overlay/ads sau khi app đã ở foreground
    page.dismiss_player_overlays()

    # 4. Tap tab Khám phá — dùng element_to_be_clickable tránh click trên element chưa sẵn sàng
    try:
        by, value = AndroidHomeLocators.BOTTOM_NAV_HOME
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((by, value))
        ).click()
    except Exception:
        pass


@pytest.fixture(scope="function", autouse=True)
def reset_to_home(driver):
    _navigate_to_home(driver)
    yield


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, driver):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        test_name = request.node.name
        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        path = f"{screenshot_dir}/{test_name}.png"
        try:
            driver.save_screenshot(path)
            print(f"\n[SCREENSHOT] Da luu tai: {path}")
        except Exception:
            pass


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
