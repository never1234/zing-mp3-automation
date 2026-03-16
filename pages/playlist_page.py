from pages.base_page import BasePage
from locators.android_locators import AndroidPlaylistLocators


class PlaylistPage(BasePage):
    """Màn hình chi tiết Playlist / Album của Zing MP3"""

    def __init__(self, driver):
        super().__init__(driver)
        self.loc = AndroidPlaylistLocators if self.platform == "android" else None

    # --------------------------------------------------
    # Kiểm tra hiển thị
    # --------------------------------------------------
    def is_playlist_visible(self):
        """Kiểm tra màn hình playlist đang hiển thị"""
        return self.is_visible(self.loc.PLAYLIST_TITLE)

    def is_song_list_visible(self):
        """Kiểm tra danh sách bài hát hiển thị"""
        return self.is_visible(self.loc.SONG_LIST)

    # --------------------------------------------------
    # Thông tin playlist
    # --------------------------------------------------
    def get_title(self):
        """Lấy tên playlist / album"""
        self.wait_for_visible(self.loc.PLAYLIST_TITLE)
        return self.get_text(self.loc.PLAYLIST_TITLE)

    def get_header_artist(self):
        """Lấy tên tác giả / nguồn playlist"""
        return self.get_text(self.loc.HEADER_ARTIST)

    def get_song_count_duration(self):
        """Lấy số bài và tổng thời gian"""
        return self.get_text(self.loc.SONG_COUNT_DURATION)

    def get_description(self):
        """Lấy mô tả playlist"""
        return self.get_text(self.loc.DESCRIPTION)

    # --------------------------------------------------
    # Hành động
    # --------------------------------------------------
    def tap_shuffle(self):
        """Nhấn nút Phát ngẫu nhiên"""
        self.wait_and_tap(self.loc.BTN_SHUFFLE)

    def tap_download(self):
        """Nhấn nút Tải xuống"""
        self.wait_and_tap(self.loc.BTN_DOWNLOAD)

    def tap_fav(self):
        """Thích / bỏ thích playlist"""
        self.wait_and_tap(self.loc.BTN_FAV)

    def tap_play_pause(self):
        """Nhấn play / pause playlist"""
        self.wait_and_tap(self.loc.BTN_PLAY_PAUSE)

    def tap_more_menu(self):
        """Mở menu Thêm (3 chấm)"""
        self.wait_and_tap(self.loc.MENU_MORE)

    def tap_add_song(self):
        """Nhấn Thêm bài vào playlist (User playlist)"""
        self.wait_and_tap(self.loc.BTN_ADD_SONG)

    # --------------------------------------------------
    # Danh sách bài hát
    # --------------------------------------------------
    def get_first_song_title(self):
        """Lấy tên bài hát đầu tiên"""
        self.wait_for_visible(self.loc.FIRST_SONG_TITLE)
        return self.get_text(self.loc.FIRST_SONG_TITLE)

    def get_first_song_artist(self):
        """Lấy tên nghệ sĩ bài hát đầu tiên"""
        return self.get_text(self.loc.FIRST_SONG_ARTIST)

    def tap_first_song(self):
        """Nhấn bài hát đầu tiên để phát"""
        self.wait_and_tap(self.loc.FIRST_SONG_TITLE)

    def tap_first_song_menu(self):
        """Mở menu của bài hát đầu tiên"""
        self.wait_and_tap(self.loc.FIRST_SONG_MENU_BTN)

    def is_download_indicator_visible(self):
        """Kiểm tra có icon đã tải không"""
        return self.is_visible(self.loc.DOWNLOAD_INDICATOR)

    def get_fav_text(self):
        """Lấy text nút Thích"""
        return self.get_text(self.loc.TV_FAV)

    # --------------------------------------------------
    # Scroll
    # --------------------------------------------------
    def scroll_song_list(self):
        """Cuộn danh sách bài hát xuống"""
        self.scroll_down()