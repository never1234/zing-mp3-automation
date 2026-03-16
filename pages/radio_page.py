from pages.base_page import BasePage
from locators.android_locators import AndroidRadioLocators


class RadioPage(BasePage):
    """Màn hình Phòng nhạc (Radio) của Zing MP3"""

    def __init__(self, driver):
        super().__init__(driver)
        self.loc = AndroidRadioLocators if self.platform == "android" else None

    # --------------------------------------------------
    # Kiểm tra hiển thị
    # --------------------------------------------------
    def is_radio_list_visible(self):
        """Kiểm tra danh sách kênh radio hiển thị"""
        return self.is_visible(self.loc.RADIO_LIST)

    def is_radio_page_visible(self):
        """Kiểm tra đang ở màn hình Radio"""
        return self.is_visible(self.loc.RADIO_LIST) or self.is_visible(self.loc.IV_CHANNEL_THUMB)

    # --------------------------------------------------
    # Thao tác
    # --------------------------------------------------
    def tap_search(self):
        """Nhấn vào icon tìm kiếm"""
        self.wait_and_tap(self.loc.SEARCH_BTN)

    def tap_first_radio_channel(self):
        """Nhấn vào kênh radio đầu tiên trong danh sách"""
        channels = self.find_all(self.loc.IV_CHANNEL_THUMB)
        if channels:
            channels[0].click()

    def tap_play_radio(self):
        """Nhấn nút phát radio"""
        self.wait_and_tap(self.loc.IV_PLAY_RADIO)

    def refresh(self):
        """Kéo để làm mới danh sách radio"""
        self.scroll_up()

    def get_radio_title(self):
        """Lấy tên kênh radio đầu tiên"""
        return self.get_text(self.loc.TV_RADIO_TITLE)

    # --------------------------------------------------
    # Radio Player
    # --------------------------------------------------
    def is_radio_player_visible(self):
        """Kiểm tra radio player đang hiển thị"""
        return self.is_visible(self.loc.RADIO_LAYOUT)

    def get_player_name(self):
        """Lấy tên kênh trong radio player"""
        return self.get_text(self.loc.RADIO_PLAYER_NAME)

    def get_player_title(self):
        """Lấy tiêu đề bài hát trong radio player"""
        return self.get_text(self.loc.RADIO_PLAYER_TITLE)

    def tap_follow(self):
        """Theo dõi / hủy theo dõi kênh radio"""
        self.wait_and_tap(self.loc.BTN_FOLLOW)

    def tap_reaction(self):
        """Nhấn nút thả tim / reaction"""
        self.wait_and_tap(self.loc.BTN_REACTION)

    def get_reaction_count(self):
        """Lấy số lượng reaction"""
        return self.get_text(self.loc.REACTION_COUNT)

    def get_viewer_count(self):
        """Lấy số người đang xem"""
        return self.get_text(self.loc.VIEWER_COUNT)

    def is_live_indicator_visible(self):
        """Kiểm tra indicator LIVE đang hiển thị"""
        return self.is_visible(self.loc.LIVE_INDICATOR)

    def close_radio_player(self):
        """Đóng radio player"""
        self.wait_and_tap(self.loc.IV_CLOSE)

    def send_chat_message(self, message: str):
        """Gửi tin nhắn trong phòng radio"""
        self.wait_and_tap(self.loc.EDT_MESSAGE)
        self.type_text(self.loc.EDT_MESSAGE, message)