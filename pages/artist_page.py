from pages.base_page import BasePage
from locators.android_locators import AndroidArtistLocators


class ArtistPage(BasePage):
    """Màn hình trang Nghệ sĩ của Zing MP3"""

    def __init__(self, driver):
        super().__init__(driver)
        self.loc = AndroidArtistLocators if self.platform == "android" else None

    # --------------------------------------------------
    # Kiểm tra hiển thị
    # --------------------------------------------------
    def is_artist_page_visible(self):
        """Kiểm tra màn hình Nghệ sĩ đang hiển thị"""
        return self.is_visible(self.loc.COLLAPSING_TOOLBAR) or self.is_visible(self.loc.IMG_COVER)

    def is_follow_btn_visible(self):
        """Kiểm tra nút theo dõi hiển thị"""
        return self.is_visible(self.loc.BTN_FOLLOW)

    # --------------------------------------------------
    # Thông tin nghệ sĩ
    # --------------------------------------------------
    def get_follower_count(self):
        """Lấy số lượng người theo dõi nghệ sĩ"""
        return self.get_text(self.loc.TV_FOLLOWER_NUMB)

    def get_first_song_title(self):
        """Lấy tên bài hát đầu tiên trong trang nghệ sĩ"""
        self.wait_for_visible(self.loc.SONG_TITLE)
        songs = self.find_all(self.loc.SONG_TITLE)
        return songs[0].text if songs else None

    # --------------------------------------------------
    # Hành động
    # --------------------------------------------------
    def tap_follow(self):
        """Nhấn theo dõi / hủy theo dõi nghệ sĩ"""
        self.wait_and_tap(self.loc.BTN_FOLLOW)

    def tap_play(self):
        """Nhấn phát nhạc nghệ sĩ"""
        self.wait_and_tap(self.loc.BTN_PLAY)

    def tap_more(self):
        """Nhấn nút Thêm (More)"""
        self.wait_and_tap(self.loc.BTN_MORE)

    def tap_menu_more(self):
        """Nhấn menu Thêm (3 chấm trên toolbar)"""
        self.wait_and_tap(self.loc.MENU_MORE)

    def tap_see_more(self):
        """Nhấn 'Xem thêm' trong section"""
        self.wait_and_tap(self.loc.TV_MORE)

    def tap_first_song(self):
        """Nhấn vào bài hát đầu tiên"""
        songs = self.find_all(self.loc.SONG_TITLE)
        if songs:
            songs[0].click()

    def tap_first_song_menu(self):
        """Nhấn menu (3 chấm) của bài hát đầu tiên"""
        menus = self.find_all(self.loc.SONG_MENU_BTN)
        if menus:
            menus[0].click()

    def refresh(self):
        """Kéo để làm mới trang nghệ sĩ"""
        self.scroll_up()

    # --------------------------------------------------
    # Trạng thái nút theo dõi
    # --------------------------------------------------
    def is_following(self):
        """Kiểm tra đã theo dõi nghệ sĩ chưa"""
        btn = self.find(self.loc.BTN_FOLLOW)
        return btn.get_attribute("selected") == "true"
