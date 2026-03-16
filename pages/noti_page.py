from pages.base_page import BasePage
from locators.android_locators import AndroidNotiLocators


class NotiPage(BasePage):
    """Màn hình Thông báo của Zing MP3"""

    def __init__(self, driver):
        super().__init__(driver)
        self.loc = AndroidNotiLocators if self.platform == "android" else None

    # --------------------------------------------------
    # Kiểm tra hiển thị
    # --------------------------------------------------
    def is_noti_page_visible(self):
        """Kiểm tra màn hình Thông báo đang hiển thị"""
        return self.is_visible(self.loc.TOOLBAR_TITLE)

    def get_toolbar_title(self):
        """Lấy tiêu đề toolbar"""
        return self.get_text(self.loc.TOOLBAR_TITLE)

    def is_noti_list_visible(self):
        """Kiểm tra danh sách thông báo hiển thị"""
        return self.is_visible(self.loc.NOTI_LIST)

    # --------------------------------------------------
    # Danh sách thông báo
    # --------------------------------------------------
    def get_first_noti_title(self):
        """Lấy tiêu đề thông báo đầu tiên"""
        self.wait_for_visible(self.loc.NOTI_TITLE)
        titles = self.find_all(self.loc.NOTI_TITLE)
        return titles[0].text if titles else None

    def get_first_noti_content(self):
        """Lấy nội dung thông báo đầu tiên"""
        contents = self.find_all(self.loc.NOTI_CONTENT)
        return contents[0].text if contents else None

    def tap_first_noti(self):
        """Nhấn vào thông báo đầu tiên"""
        titles = self.find_all(self.loc.NOTI_TITLE)
        if titles:
            titles[0].click()

    def get_noti_count(self):
        """Lấy số lượng thông báo hiển thị"""
        return len(self.find_all(self.loc.NOTI_TITLE))

    # --------------------------------------------------
    # Làm mới
    # --------------------------------------------------
    def refresh(self):
        """Kéo để làm mới danh sách thông báo"""
        self.scroll_up()
