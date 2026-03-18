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
        self.minimize_player()

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

    # --------------------------------------------------
    # Bottom Banner (Free / Non-login)
    # --------------------------------------------------
    def is_bottom_banner_visible(self):
        """Kiểm tra banner upgrade hiển thị"""
        return self.is_visible(self.loc.BOTTOM_BANNER)

    def get_bottom_banner_title(self):
        """Lấy tiêu đề banner upgrade"""
        return self.get_text(self.loc.BOTTOM_BANNER_TITLE)

    # --------------------------------------------------
    # Bottom Sheet (More options)
    # --------------------------------------------------
    def tap_more_btn(self):
        """Mở menu Thêm (bottom sheet)"""
        self.wait_and_tap(self.loc.MENU_MORE_BTN)

    def tap_bottom_sheet_share(self):
        """Nhấn Chia sẻ trong bottom sheet"""
        self.wait_and_tap(self.loc.BOTTOM_SHEET_SHARE)

    def tap_bottom_sheet_timer(self):
        """Nhấn Hẹn giờ tắt trong bottom sheet"""
        self.wait_and_tap(self.loc.BOTTOM_SHEET_TIMER)

    def get_bottom_sheet_timer_text(self):
        """Lấy text hẹn giờ"""
        return self.get_text(self.loc.BOTTOM_SHEET_TIMER)

    # --------------------------------------------------
    # Queue (Danh sách phát)
    # --------------------------------------------------
    def tap_queue(self):
        """Mở danh sách phát"""
        self.wait_and_tap(self.loc.QUEUE_BTN)

    def is_queue_visible(self):
        """Kiểm tra danh sách phát đang mở"""
        return self.is_visible(self.loc.QUEUE_CLOSE_BTN)

    def close_queue(self):
        """Đóng danh sách phát"""
        self.wait_and_tap(self.loc.QUEUE_CLOSE_BTN)

    def get_queue_songs(self):
        """Lấy danh sách tên bài hát trong queue"""
        from appium.webdriver.common.appiumby import AppiumBy
        items = self.find_all((AppiumBy.ID, "com.zing.mp3:id/tvTitle"))
        return [item.text for item in items]

    # --------------------------------------------------
    # Lyrics
    # --------------------------------------------------
    def is_lyrics_visible(self):
        """Kiểm tra lời bài hát đang hiển thị"""
        return self.is_visible(self.loc.LYRIC_TEXT) or self.is_visible(self.loc.LYRIC_RECYCLER)

    def get_lyric_text(self):
        """Lấy text lyrics (view đơn giản)"""
        return self.get_text(self.loc.LYRIC_TEXT)

    def tap_deep_lyric(self):
        """Nhấn nút Deep Lyric theme"""
        self.wait_and_tap(self.loc.DEEP_LYRIC_BTN)

    # --------------------------------------------------
    # Song Info
    # --------------------------------------------------
    def get_song_album(self):
        """Lấy tên album trong Song Info"""
        return self.get_text(self.loc.SONG_INFO_ALBUM)

    def get_song_composer(self):
        """Lấy tên nhạc sĩ sáng tác"""
        return self.get_text(self.loc.SONG_INFO_COMPOSER)

    def get_song_plays(self):
        """Lấy số lượt nghe"""
        return self.get_text(self.loc.SONG_INFO_PLAYS)

    def get_song_favs(self):
        """Lấy số lượt thích"""
        return self.get_text(self.loc.SONG_INFO_FAVS)

    # --------------------------------------------------
    # Reward Ads (Free)
    # --------------------------------------------------
    def is_reward_ads_visible(self):
        """Kiểm tra nút Reward Ads hiển thị"""
        return self.is_visible(self.loc.BTN_REWARD_ADS)

    def tap_reward_ads(self):
        """Nhấn nút xem quảng cáo để mở khóa"""
        self.wait_and_tap(self.loc.BTN_REWARD_ADS)
