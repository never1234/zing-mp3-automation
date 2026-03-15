from pages.base_page import BasePage
from locators.android_locators import AndroidSearchLocators
from locators.ios_locators import IOSSearchLocators


class SearchPage(BasePage):
    """Màn hình Tìm kiếm của Zing MP3"""

    def __init__(self, driver):
        super().__init__(driver)
        self.loc = AndroidSearchLocators if self.platform == "android" else IOSSearchLocators

    def search_song(self, keyword: str):
        """Tìm kiếm bài hát theo từ khóa"""
        self.wait_and_tap(self.loc.SEARCH_BAR)
        self.type_text(self.loc.SEARCH_INPUT, keyword)
        # Submit tìm kiếm
        self.driver.execute_script("mobile: pressKey", {"keycode": 66}) \
            if self.platform == "android" \
            else self.driver.execute_script("mobile: typeText", {"text": "\n"})

    def get_first_result_name(self):
        """Lấy tên bài hát đầu tiên trong kết quả tìm kiếm"""
        self.wait_for_visible(self.loc.FIRST_SONG_RESULT)
        return self.get_text(self.loc.FIRST_SONG_RESULT)

    def tap_first_result(self):
        """Nhấn vào bài hát đầu tiên trong kết quả"""
        self.wait_and_tap(self.loc.FIRST_SONG_RESULT)

    def is_no_result_shown(self):
        """Kiểm tra có hiện thông báo 'không có kết quả' không"""
        return self.is_visible(self.loc.NO_RESULT_TEXT)

    def get_result_count(self):
        """Lấy số lượng kết quả tìm kiếm"""
        results = self.find_all(self.loc.SONG_LIST)
        return len(results)
