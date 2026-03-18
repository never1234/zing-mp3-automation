import os
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """
    Base Page — chứa các hàm dùng chung cho cả Android & iOS
    Tất cả Page Object đều kế thừa class này
    """

    def __init__(self, driver):
        self.driver   = driver
        # Tự động nhận biết platform từ biến môi trường
        self.platform = os.getenv("PLATFORM", "android").lower()

    # --------------------------------------------------
    # Tìm element
    # --------------------------------------------------
    def find(self, locator):
        """Tìm 1 element theo locator (by, value)"""
        by, value = locator
        return self.driver.find_element(by, value)

    def find_all(self, locator):
        """Tìm nhiều element theo locator"""
        by, value = locator
        return self.driver.find_elements(by, value)

    # --------------------------------------------------
    # Thao tác cơ bản
    # --------------------------------------------------
    def tap(self, locator):
        """Nhấn vào element"""
        self.find(locator).click()

    def type_text(self, locator, text):
        """Xóa rồi gõ text vào input"""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Lấy text của element"""
        return self.find(locator).text

    def is_visible(self, locator):
        """Kiểm tra element có hiển thị không (không chờ)"""
        try:
            return self.find(locator).is_displayed()
        except (NoSuchElementException, Exception):
            return False

    def is_visible_with_wait(self, locator, timeout=5):
        """Chờ tối đa timeout giây rồi trả về True/False — tránh false-negative sau screen transition"""
        try:
            self.wait_for_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    # --------------------------------------------------
    # Chờ element
    # --------------------------------------------------
    def wait_for_visible(self, locator, timeout=10):
        """Chờ element hiển thị trong vòng timeout giây"""
        by, value = locator
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except TimeoutException:
            raise TimeoutException(f"Element không hiển thị sau {timeout}s: {locator}")

    def wait_for_clickable(self, locator, timeout=10):
        """Chờ element có thể click được"""
        by, value = locator
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def wait_and_tap(self, locator, timeout=10):
        """Chờ rồi nhấn"""
        self.wait_for_clickable(locator, timeout).click()

    # --------------------------------------------------
    # Scroll
    # --------------------------------------------------
    def scroll_and_tap(self, locator, max_scrolls=5, timeout=5):
        """Cuộn xuống và tap element. Thử tối đa max_scrolls lần scroll_down trước khi tap.
        An toàn hơn UIScrollable — không gây treo UiAutomator2 server.
        """
        for _ in range(max_scrolls):
            try:
                self.wait_and_tap(locator, timeout=timeout)
                return
            except Exception:
                self.scroll_down()
        self.wait_and_tap(locator)

    def scroll_down(self):
        """Cuộn xuống"""
        size   = self.driver.get_window_size()
        width  = size["width"]
        height = size["height"]
        self.driver.swipe(
            start_x=width // 2, start_y=int(height * 0.7),
            end_x=width // 2,   end_y=int(height * 0.3),
            duration=500
        )

    def scroll_up(self):
        """Cuộn lên"""
        size   = self.driver.get_window_size()
        width  = size["width"]
        height = size["height"]
        self.driver.swipe(
            start_x=width // 2, start_y=int(height * 0.3),
            end_x=width // 2,   end_y=int(height * 0.7),
            duration=500
        )

    # --------------------------------------------------
    # Auto-dismiss Player overlays
    # --------------------------------------------------
    def dismiss_player_overlays(self):
        """Tự động đóng các dialog/popup/ads trong màn hình Player (nếu có).
        An toàn để gọi bất kỳ lúc nào — không raise nếu không có overlay.

        Handles:
        - Reward Ads overlay (Ads-Reward): layoutCountdown + btnCta
        - Lossless BTS (Player-Bts-Lossless): design_bottom_sheet + btnNegative "ĐỂ SAU"
        - Promotion popup: btnNegative "Không phải bây giờ" / "Bỏ qua"
        """
        from locators.android_locators import AndroidPlayerLocators, AndroidHomeLocators

        # 1. Reward Ads overlay — chặn Player khi non-premium trigger reward ad
        if self.is_visible(AndroidPlayerLocators.ADS_REWARD_LAYOUT):
            try:
                self.tap(AndroidPlayerLocators.ADS_REWARD_CTA_BTN)
            except Exception:
                pass

        # 2. Lossless BTS + Promotion popup — cùng dùng btnNegative để dismiss
        # Dùng is_visible_with_wait để chờ sheet render (xuất hiện trước khi Player load xong)
        if self.is_visible_with_wait(AndroidHomeLocators.POPUP_SKIP_BTN, timeout=5):
            try:
                self.tap(AndroidHomeLocators.POPUP_SKIP_BTN)
            except Exception:
                pass

    def minimize_player(self):
        """Thu nhỏ full Player về mini player bằng Android back button.
        Đáng tin cậy hơn tap MINIMIZE_BTN vì không phụ thuộc vào accessibility label.
        """
        self.driver.back()

    def dismiss_app_theme_sheet(self):
        """Đóng bottom sheet 'Chọn chủ đề' (App Theme) nếu đang hiển thị.
        Chờ tối đa 3 giây để sheet xuất hiện (tránh bỏ sót khi sheet load chậm).
        An toàn để gọi bất kỳ lúc nào — không raise nếu sheet không xuất hiện.
        """
        from locators.android_locators import AndroidPlayerLocators
        if self.is_visible_with_wait(AndroidPlayerLocators.BTS_APP_THEME_TITLE, timeout=3):
            try:
                self.tap(AndroidPlayerLocators.BTS_APP_THEME_CLOSE)
            except Exception:
                pass

    # --------------------------------------------------
    # Chụp màn hình khi lỗi
    # --------------------------------------------------
    def take_screenshot(self, name="screenshot"):
        """Chụp màn hình lưu vào reports/"""
        import os
        os.makedirs("reports/screenshots", exist_ok=True)
        path = f"reports/screenshots/{name}.png"
        self.driver.save_screenshot(path)
        return path
