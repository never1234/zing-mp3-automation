import os
from pages.base_page import BasePage
from locators.android_locators import AndroidLoginLocators
from locators.ios_locators import IOSLoginLocators


class LoginPage(BasePage):
    """Màn hình Đăng nhập của Zing MP3"""

    def __init__(self, driver):
        super().__init__(driver)
        self.loc = AndroidLoginLocators if self.platform == "android" else IOSLoginLocators

    def tap_login_button(self):
        """Nhấn nút Đăng nhập từ màn hình chính"""
        self.wait_and_tap(self.loc.LOGIN_BTN)

    def login(self, email: str = None, password: str = None):
        """
        Đăng nhập bằng email và mật khẩu
        Mặc định lấy từ biến môi trường trong .env
        """
        email    = email    or os.getenv("ZING_TEST_EMAIL", "")
        password = password or os.getenv("ZING_TEST_PASSWORD", "")

        self.wait_for_visible(self.loc.EMAIL_INPUT)
        self.type_text(self.loc.EMAIL_INPUT, email)
        self.type_text(self.loc.PASSWORD_INPUT, password)
        self.tap(self.loc.SUBMIT_BTN)

    def get_error_message(self):
        """Lấy thông báo lỗi khi đăng nhập thất bại"""
        self.wait_for_visible(self.loc.ERROR_MSG)
        return self.get_text(self.loc.ERROR_MSG)

    def is_logged_in(self):
        """Kiểm tra đã đăng nhập thành công (avatar hiển thị)"""
        return self.is_visible(self.loc.AVATAR)
