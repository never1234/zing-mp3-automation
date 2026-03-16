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

    def clear_search(self):
        """Nhấn nút xóa text tìm kiếm"""
        self.wait_and_tap(self.loc.SEARCH_CLEAR_BTN)

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

    # --------------------------------------------------
    # Tabs kết quả
    # --------------------------------------------------
    def tap_tab_noi_bat(self):
        """Chuyển sang tab Nổi bật"""
        self.wait_and_tap(self.loc.TAB_NOI_BAT)

    def tap_tab_bai_hat(self):
        """Chuyển sang tab Bài hát"""
        self.wait_and_tap(self.loc.TAB_BAI_HAT)

    def tap_tab_mv(self):
        """Chuyển sang tab MV"""
        self.wait_and_tap(self.loc.TAB_MV)

    def tap_tab_nghe_si(self):
        """Chuyển sang tab Nghệ sĩ"""
        self.wait_and_tap(self.loc.TAB_NGHE_SI)

    def tap_tab_playlist(self):
        """Chuyển sang tab Playlist"""
        self.wait_and_tap(self.loc.TAB_PLAYLIST)

    # --------------------------------------------------
    # Từ khóa gần đây
    # --------------------------------------------------
    def get_recent_keywords(self):
        """Lấy danh sách từ khóa gần đây"""
        chips = self.find_all(self.loc.KEYWORD_CHIP)
        return [chip.text for chip in chips]

    def tap_recent_keyword(self, index: int = 0):
        """Nhấn vào từ khóa gần đây theo index (0-based)"""
        chips = self.find_all(self.loc.KEYWORD_CHIP)
        if chips and index < len(chips):
            chips[index].click()

    def is_search_layout_visible(self):
        """Kiểm tra layout tìm kiếm đang hiển thị"""
        return self.is_visible(self.loc.SEARCH_LAYOUT)

    # --------------------------------------------------
    # Item trong kết quả
    # --------------------------------------------------
    def get_result_titles(self):
        """Lấy tất cả tên trong danh sách kết quả"""
        items = self.find_all(self.loc.ITEM_TITLE)
        return [item.text for item in items]

    def tap_item_more_btn(self, index: int = 0):
        """Nhấn nút menu (3 chấm) của item theo index"""
        menus = self.find_all(self.loc.ITEM_MORE_BTN)
        if menus and index < len(menus):
            menus[index].click()
