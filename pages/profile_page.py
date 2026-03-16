from pages.base_page import BasePage
from locators.android_locators import AndroidProfileLocators


class ProfilePage(BasePage):
    """Màn hình Cá nhân của Zing MP3"""

    def __init__(self, driver):
        super().__init__(driver)
        self.loc = AndroidProfileLocators if self.platform == "android" else None

    # --------------------------------------------------
    # Kiểm tra trạng thái đăng nhập
    # --------------------------------------------------
    def is_logged_in(self):
        """Kiểm tra đã đăng nhập chưa (có hiển thị tên người dùng)"""
        return self.is_visible(self.loc.USER_NAME)

    def is_non_login_state(self):
        """Kiểm tra chưa đăng nhập (có nút ĐĂNG NHẬP)"""
        return self.is_visible(self.loc.BTN_LOGIN)

    def is_profile_visible(self):
        """Kiểm tra màn hình Cá nhân đang hiển thị"""
        return self.is_visible(self.loc.AVATAR)

    # --------------------------------------------------
    # Thông tin người dùng
    # --------------------------------------------------
    def get_user_name(self):
        """Lấy tên người dùng"""
        self.wait_for_visible(self.loc.USER_NAME)
        return self.get_text(self.loc.USER_NAME)

    def get_plan_countdown(self):
        """Lấy text đếm ngược kết thúc gói Premium"""
        return self.get_text(self.loc.PLAN_COUNTDOWN)

    # --------------------------------------------------
    # Hành động đăng nhập / đăng xuất
    # --------------------------------------------------
    def tap_login(self):
        """Nhấn nút ĐĂNG NHẬP"""
        self.wait_and_tap(self.loc.BTN_LOGIN)

    def tap_avatar(self):
        """Nhấn vào avatar"""
        self.wait_and_tap(self.loc.AVATAR)

    # --------------------------------------------------
    # Quản lý gói
    # --------------------------------------------------
    def tap_manage_plan(self):
        """Nhấn 'Quản lý gói đã dùng'"""
        self.wait_and_tap(self.loc.BTN_MANAGE_PLAN)

    def tap_enter_code(self):
        """Nhấn 'Nhập Code'"""
        self.wait_and_tap(self.loc.BTN_ENTER_CODE)

    # --------------------------------------------------
    # Premium upsell
    # --------------------------------------------------
    def is_upsell_visible(self):
        """Kiểm tra card upsell Premium hiển thị"""
        return self.is_visible(self.loc.UPSELL_CARD)

    def get_upsell_price(self):
        """Lấy giá upsell"""
        return self.get_text(self.loc.UPSELL_PRICE)

    def get_upsell_desc(self):
        """Lấy mô tả upsell"""
        return self.get_text(self.loc.UPSELL_DESC)

    def get_benefit_no_ads(self):
        """Lấy nội dung lợi ích 'Loại bỏ quảng cáo'"""
        return self.get_text(self.loc.BENEFIT_NO_ADS)

    def get_benefit_download(self):
        """Lấy nội dung lợi ích 'Tải nhạc'"""
        return self.get_text(self.loc.BENEFIT_DOWNLOAD)

    def get_benefit_order_play(self):
        """Lấy nội dung lợi ích 'Phát theo thứ tự'"""
        return self.get_text(self.loc.BENEFIT_ORDER_PLAY)

    def get_feature_theme(self):
        """Lấy nội dung tính năng 'Tùy chỉnh giao diện'"""
        return self.get_text(self.loc.FEATURE_THEME)

    def get_feature_lossless(self):
        """Lấy nội dung tính năng 'Âm thanh Lossless'"""
        return self.get_text(self.loc.FEATURE_LOSSLESS)

    # --------------------------------------------------
    # Scroll
    # --------------------------------------------------
    def scroll_to_upsell(self):
        """Cuộn xuống để thấy card upsell"""
        for _ in range(3):
            if self.is_visible(self.loc.UPSELL_CARD):
                break
            self.scroll_down()