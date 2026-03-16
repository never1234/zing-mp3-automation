from pages.base_page import BasePage
from locators.android_locators import AndroidRecentLocators


class RecentPage(BasePage):
    """Màn hình Nghe gần đây của Zing MP3"""

    def __init__(self, driver):
        super().__init__(driver)
        self.loc = AndroidRecentLocators if self.platform == "android" else None

    # --------------------------------------------------
    # Kiểm tra hiển thị
    # --------------------------------------------------
    def is_recent_page_visible(self):
        """Kiểm tra màn hình Nghe gần đây đang hiển thị"""
        return self.is_visible(self.loc.TOOLBAR_TITLE)

    def get_toolbar_title(self):
        """Lấy tiêu đề toolbar"""
        return self.get_text(self.loc.TOOLBAR_TITLE)

    # --------------------------------------------------
    # Điều hướng tabs
    # --------------------------------------------------
    def tap_tab_bai_hat(self):
        """Chuyển sang tab Bài hát"""
        self.wait_and_tap(self.loc.TAB_BAI_HAT)

    def tap_tab_playlist(self):
        """Chuyển sang tab Playlist"""
        self.wait_and_tap(self.loc.TAB_PLAYLIST)

    def tap_tab_nghe_si(self):
        """Chuyển sang tab Nghệ sĩ"""
        self.wait_and_tap(self.loc.TAB_NGHE_SI)

    def tap_tab_mv(self):
        """Chuyển sang tab MV"""
        self.wait_and_tap(self.loc.TAB_MV)

    def tap_tab_phong_nhac(self):
        """Chuyển sang tab Phòng nhạc"""
        self.wait_and_tap(self.loc.TAB_PHONG_NHAC)

    # --------------------------------------------------
    # Danh sách
    # --------------------------------------------------
    def get_first_song_title(self):
        """Lấy tên bài hát / item đầu tiên"""
        self.wait_for_visible(self.loc.SONG_TITLE)
        titles = self.find_all(self.loc.SONG_TITLE)
        return titles[0].text if titles else None

    def get_first_song_artist(self):
        """Lấy tên nghệ sĩ của item đầu tiên"""
        artists = self.find_all(self.loc.SONG_ARTIST)
        return artists[0].text if artists else None

    def tap_first_song(self):
        """Nhấn vào bài hát / item đầu tiên"""
        self.wait_for_visible(self.loc.SONG_TITLE)
        titles = self.find_all(self.loc.SONG_TITLE)
        if titles:
            titles[0].click()

    def tap_first_song_menu(self):
        """Nhấn menu (3 chấm) của item đầu tiên"""
        menus = self.find_all(self.loc.SONG_MENU)
        if menus:
            menus[0].click()

    def tap_shuffle(self):
        """Phát ngẫu nhiên tất cả bài gần đây"""
        self.wait_and_tap(self.loc.BTN_SHUFFLE)

    def tap_more_menu(self):
        """Mở menu Thêm (3 chấm trên header)"""
        self.wait_and_tap(self.loc.MENU_MORE)

    def get_item_count(self):
        """Lấy số lượng item trong danh sách"""
        return len(self.find_all(self.loc.SONG_TITLE))

    # --------------------------------------------------
    # Nghệ sĩ
    # --------------------------------------------------
    def tap_follow_first_artist(self):
        """Theo dõi nghệ sĩ đầu tiên"""
        follows = self.find_all(self.loc.BTN_FOLLOW)
        if follows:
            follows[0].click()

    def get_artist_subtitle(self):
        """Lấy subtitle nghệ sĩ (số người theo dõi)"""
        subtitles = self.find_all(self.loc.ARTIST_SUBTITLE)
        return subtitles[0].text if subtitles else None

    # --------------------------------------------------
    # MV
    # --------------------------------------------------
    def get_first_mv_duration(self):
        """Lấy thời lượng MV đầu tiên"""
        durations = self.find_all(self.loc.MV_DURATION)
        return durations[0].text if durations else None
