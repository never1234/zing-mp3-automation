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
        """Kiểm tra element có hiển thị không"""
        try:
            return self.find(locator).is_displayed()
        except (NoSuchElementException, Exception):
            return False

    # --------------------------------------------------
    # Chờ element
    # --------------------------------------------------
    def wait_for_visible(self, locator, timeout=10):
        """Chờ element hiển thị trong vòng timeout giây"""
        by, value = locator
        self.driver.implicitly_wait(0)  # tắt implicit wait để tránh xung đột với explicit wait
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except TimeoutException:
            raise TimeoutException(f"Element không hiển thị sau {timeout}s: {locator}")
        finally:
            self.driver.implicitly_wait(10)  # khôi phục

    def wait_for_clickable(self, locator, timeout=10):
        """Chờ element có thể click được"""
        by, value = locator
        self.driver.implicitly_wait(0)  # tắt implicit wait để tránh xung đột với explicit wait
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
        finally:
            self.driver.implicitly_wait(10)  # khôi phục

    def wait_and_tap(self, locator, timeout=10):
        """Chờ rồi nhấn"""
        self.wait_for_clickable(locator, timeout).click()

    # --------------------------------------------------
    # Scroll
    # --------------------------------------------------
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
    # Chụp màn hình khi lỗi
    # --------------------------------------------------
    def take_screenshot(self, name="screenshot"):
        """Chụp màn hình lưu vào reports/"""
        import os
        os.makedirs("reports/screenshots", exist_ok=True)
        path = f"reports/screenshots/{name}.png"
        self.driver.save_screenshot(path)
        return path
