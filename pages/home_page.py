from pages.base_page import BasePage
from locators.android_locators import AndroidHomeLocators
from locators.ios_locators import IOSHomeLocators


class HomePage(BasePage):
    """Màn hình Khám phá (Home) của Zing MP3"""

    def __init__(self, driver):
        super().__init__(driver)
        self.loc = AndroidHomeLocators if self.platform == "android" else IOSHomeLocators

    def tap_search(self):
        """Nhấn vào icon tìm kiếm"""
        self.wait_and_tap(self.loc.SEARCH_BUTTON)

    def tap_bottom_nav(self, tab: str):
        """
        Nhấn tab dưới cùng
        tab: 'home' | 'chart' | 'radio' | 'library' | 'profile'
        """
        nav_map = {
            "home":    self.loc.BOTTOM_NAV_HOME,
            "chart":   self.loc.BOTTOM_NAV_CHART,
            "radio":   self.loc.BOTTOM_NAV_RADIO,
            "library": self.loc.BOTTOM_NAV_LIBRARY,
            "profile": self.loc.BOTTOM_NAV_PROFILE,
        }
        if tab not in nav_map:
            raise ValueError(f"Tab không hợp lệ: {tab}")
        self.wait_and_tap(nav_map[tab])

    def tap_kham_pha(self):
        """Nhấn tab Khám phá (tab Home) trên bottom navigation"""
        self.wait_and_tap(self.loc.BOTTOM_NAV_HOME)

    def tap_quick_play_first_item(self):
        """Nhấn vào bài hát đầu tiên trong section Phát nhanh"""
        self.wait_and_tap(self.loc.QUICK_PLAY_FIRST_ITEM)

    def is_mini_player_visible(self):
        """Kiểm tra mini player đang hiển thị"""
        return self.is_visible(self.loc.MINI_PLAYER)

    def tap_mini_player(self):
        """Nhấn vào mini player để mở full player"""
        self.wait_and_tap(self.loc.MINI_PLAYER)
