from pages.base_page import BasePage
from locators.android_locators import AndroidPlayerLocators
from locators.ios_locators import IOSPlayerLocators


class PlayerPage(BasePage):
    """Màn hình Player của Zing MP3"""

    def __init__(self, driver):
        super().__init__(driver)
        self.loc = AndroidPlayerLocators if self.platform == "android" else IOSPlayerLocators

    # --------------------------------------------------
    # Thông tin bài hát
    # --------------------------------------------------
    def get_song_title(self):
        """Lấy tên bài hát đang phát"""
        self.wait_for_visible(self.loc.SONG_TITLE)
        return self.get_text(self.loc.SONG_TITLE)

    def get_artist_name(self):
        """Lấy tên nghệ sĩ"""
        return self.get_text(self.loc.ARTIST_NAME)

    def is_player_visible(self):
        """Kiểm tra player đang hiển thị"""
        return self.is_visible(self.loc.SONG_TITLE)

    # --------------------------------------------------
    # Điều khiển phát nhạc
    # --------------------------------------------------
    def tap_play_pause(self):
        """Nhấn play/pause"""
        self.wait_and_tap(self.loc.PLAY_PAUSE_BTN)

    def tap_next(self):
        """Chuyển bài kế tiếp"""
        self.wait_and_tap(self.loc.NEXT_BTN)

    def tap_prev(self):
        """Quay lại bài trước"""
        self.wait_and_tap(self.loc.PREV_BTN)

    def tap_shuffle(self):
        """Bật/tắt phát ngẫu nhiên"""
        self.wait_and_tap(self.loc.SHUFFLE_BTN)

    def tap_repeat(self):
        """Bật/tắt phát lại"""
        self.wait_and_tap(self.loc.REPEAT_BTN)

    def tap_like(self):
        """Thích/bỏ thích bài hát"""
        self.wait_and_tap(self.loc.HEART_BTN)

    def tap_minimize(self):
        """Gập player xuống thành mini player"""
        self.wait_and_tap(self.loc.MINIMIZE_BTN)

    # --------------------------------------------------
    # Trạng thái
    # --------------------------------------------------
    def is_shuffle_active(self):
        """Kiểm tra shuffle đang bật không"""
        btn = self.find(self.loc.SHUFFLE_BTN)
        if self.platform == "android":
            return btn.get_attribute("selected") == "true"
        else:
            return btn.get_attribute("value") == "1"

    def is_repeat_active(self):
        """Kiểm tra repeat đang bật không"""
        btn = self.find(self.loc.REPEAT_BTN)
        if self.platform == "android":
            return btn.get_attribute("selected") == "true"
        else:
            return btn.get_attribute("value") == "1"

    def is_progress_bar_visible(self):
        """Kiểm tra thanh tiến trình hiển thị"""
        return self.is_visible(self.loc.PROGRESS_BAR)
