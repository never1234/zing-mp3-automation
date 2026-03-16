from pages.base_page import BasePage
from locators.android_locators import AndroidSettingsLocators


class SettingsPage(BasePage):
    """Màn hình Cài đặt của Zing MP3"""

    def __init__(self, driver):
        super().__init__(driver)
        self.loc = AndroidSettingsLocators if self.platform == "android" else None

    # --------------------------------------------------
    # Kiểm tra hiển thị
    # --------------------------------------------------
    def is_settings_visible(self):
        """Kiểm tra màn hình Cài đặt đang hiển thị"""
        return self.is_visible(self.loc.TOOLBAR_TITLE)

    def get_toolbar_title(self):
        """Lấy tiêu đề toolbar"""
        return self.get_text(self.loc.TOOLBAR_TITLE)

    def get_app_version(self):
        """Lấy phiên bản ứng dụng"""
        return self.get_text(self.loc.TV_VERSION)

    # --------------------------------------------------
    # Nhấn các mục cài đặt
    # --------------------------------------------------
    def tap_download_setting(self):
        """Mở cài đặt Tải về"""
        self.wait_and_tap(self.loc.SETTING_DOWNLOAD)

    def tap_player_setting(self):
        """Mở cài đặt Trình phát"""
        self.wait_and_tap(self.loc.SETTING_PLAYER)

    def tap_notification_setting(self):
        """Mở cài đặt Thông báo"""
        self.wait_and_tap(self.loc.SETTING_NOTIFICATION)

    def tap_headset_setting(self):
        """Mở cài đặt Tai nghe"""
        self.wait_and_tap(self.loc.SETTING_HEADSET)

    def tap_video_setting(self):
        """Mở cài đặt Video"""
        self.wait_and_tap(self.loc.SETTING_VIDEO)

    def tap_library_setting(self):
        """Mở cài đặt Thư viện"""
        self.wait_and_tap(self.loc.SETTING_LIBRARY)

    def tap_theme_setting(self):
        """Mở cài đặt Giao diện"""
        self.wait_and_tap(self.loc.SETTING_THEME_LAYOUT)

    # --------------------------------------------------
    # Mục khác
    # --------------------------------------------------
    def tap_rate_me(self):
        """Nhấn Đánh giá ứng dụng"""
        self.wait_and_tap(self.loc.RATE_ME)

    def tap_feedback(self):
        """Nhấn Phản hồi & Báo cáo"""
        self.wait_and_tap(self.loc.FEEDBACK_REPORT)

    def tap_about_us(self):
        """Nhấn Về chúng tôi"""
        self.wait_and_tap(self.loc.ABOUT_US)

    def tap_privacy(self):
        """Nhấn Chính sách bảo mật"""
        self.wait_and_tap(self.loc.PRIVACY)

    def tap_terms(self):
        """Nhấn Điều khoản sử dụng"""
        self.wait_and_tap(self.loc.TERMS)

    def tap_logout(self):
        """Nhấn Đăng xuất (chỉ có khi đã đăng nhập)"""
        self.wait_and_tap(self.loc.LOGOUT)

    def is_logout_visible(self):
        """Kiểm tra nút Đăng xuất có hiển thị không"""
        return self.is_visible(self.loc.LOGOUT)

    # --------------------------------------------------
    # Kiểm tra từng mục
    # --------------------------------------------------
    def is_download_setting_visible(self):
        return self.is_visible(self.loc.SETTING_DOWNLOAD)

    def is_player_setting_visible(self):
        return self.is_visible(self.loc.SETTING_PLAYER)

    def is_notification_setting_visible(self):
        return self.is_visible(self.loc.SETTING_NOTIFICATION)

    def get_theme_name(self):
        """Lấy tên giao diện đang chọn"""
        return self.get_text(self.loc.TV_SETTING_THEME)
