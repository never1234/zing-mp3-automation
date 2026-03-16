from pages.base_page import BasePage
from locators.android_locators import AndroidMyMusicLocators


class MyMusicPage(BasePage):
    """Màn hình Thư viện (My Music) của Zing MP3"""

    def __init__(self, driver):
        super().__init__(driver)
        self.loc = AndroidMyMusicLocators if self.platform == "android" else None

    # --------------------------------------------------
    # Kiểm tra hiển thị
    # --------------------------------------------------
    def is_my_music_visible(self):
        """Kiểm tra đang ở màn hình Thư viện"""
        return self.is_visible(self.loc.TABS) or self.is_visible(self.loc.RECYCLER_VIEW)

    def is_recent_section_visible(self):
        """Kiểm tra section 'Nghe gần đây' hiển thị"""
        return self.is_visible(self.loc.RECENT_HEADER)

    def is_empty_state(self):
        """Kiểm tra trạng thái chưa đăng nhập / rỗng"""
        return self.is_visible(self.loc.TV_CLOSE_AD) or self.is_visible(self.loc.ERR_TITLE)

    # --------------------------------------------------
    # Điều hướng tabs
    # --------------------------------------------------
    def tap_playlist_tab(self):
        """Nhấn tab Playlist"""
        self.wait_and_tap(self.loc.TAB_PLAYLIST)

    def tap_album_tab(self):
        """Nhấn tab Album"""
        self.wait_and_tap(self.loc.TAB_ALBUM)

    # --------------------------------------------------
    # Tìm kiếm
    # --------------------------------------------------
    def tap_search(self):
        """Nhấn icon tìm kiếm trong thư viện"""
        self.wait_and_tap(self.loc.SEARCH_BTN)

    def tap_menu_search(self):
        """Nhấn menu tìm kiếm trong downloaded"""
        self.wait_and_tap(self.loc.MENU_SEARCH)

    # --------------------------------------------------
    # Phát nhạc
    # --------------------------------------------------
    def tap_play_pause(self):
        """Nhấn play/pause trong header thư viện"""
        self.wait_and_tap(self.loc.BTN_PLAY_PAUSE)

    def tap_shuffle(self):
        """Nhấn phát ngẫu nhiên"""
        self.wait_and_tap(self.loc.BTN_SHUFFLE)

    def tap_play(self):
        """Nhấn phát tất cả"""
        self.wait_and_tap(self.loc.BTN_PLAY)

    # --------------------------------------------------
    # Danh sách bài hát
    # --------------------------------------------------
    def get_first_song_title(self):
        """Lấy tên bài hát đầu tiên"""
        self.wait_for_visible(self.loc.SONG_TITLE)
        songs = self.find_all(self.loc.SONG_TITLE)
        return songs[0].text if songs else None

    def tap_first_song(self):
        """Nhấn vào bài hát đầu tiên"""
        songs = self.find_all(self.loc.SONG_TITLE)
        if songs:
            songs[0].click()

    def tap_first_song_menu(self):
        """Nhấn nút menu (3 chấm) của bài hát đầu tiên"""
        menus = self.find_all(self.loc.SONG_MENU)
        if menus:
            menus[0].click()

    def get_song_count_text(self):
        """Lấy text số lượng bài hát"""
        return self.get_text(self.loc.TV_COUNT)

    # --------------------------------------------------
    # Filter / Sort
    # --------------------------------------------------
    def tap_filter(self):
        """Mở bộ lọc"""
        self.wait_and_tap(self.loc.IMG_FILTER)

    def get_current_filter(self):
        """Lấy tên bộ lọc đang chọn"""
        return self.get_text(self.loc.TV_FILTER)

    def get_current_sort(self):
        """Lấy kiểu sắp xếp đang chọn"""
        return self.get_text(self.loc.TV_SORT)

    # --------------------------------------------------
    # More menu
    # --------------------------------------------------
    def tap_more_menu(self):
        """Nhấn menu Thêm"""
        self.wait_and_tap(self.loc.MENU_MORE)

    def tap_download_menu(self):
        """Nhấn menu Tải về"""
        self.wait_and_tap(self.loc.MENU_DOWNLOAD)

    # --------------------------------------------------
    # Error state
    # --------------------------------------------------
    def get_error_title(self):
        """Lấy tiêu đề lỗi / trống"""
        return self.get_text(self.loc.ERR_TITLE)

    def get_error_message(self):
        """Lấy nội dung lỗi / trống"""
        return self.get_text(self.loc.ERR_MSG)