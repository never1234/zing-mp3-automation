from pages.base_page import BasePage
from locators.android_locators import AndroidSubscriptionLocators


class SubscriptionPage(BasePage):
    """Màn hình Đăng ký gói / Nâng cấp tài khoản của Zing MP3"""

    def __init__(self, driver):
        super().__init__(driver)
        self.loc = AndroidSubscriptionLocators if self.platform == "android" else None

    # --------------------------------------------------
    # Kiểm tra hiển thị
    # --------------------------------------------------
    def is_package_list_visible(self):
        """Kiểm tra màn hình danh sách gói hiển thị"""
        return self.is_visible(self.loc.PACKAGE_LIST)

    def is_package_detail_visible(self):
        """Kiểm tra màn hình chi tiết gói hiển thị"""
        return self.is_visible(self.loc.BTN_BOTTOM_CTA)

    # --------------------------------------------------
    # Danh sách gói
    # --------------------------------------------------
    def get_package_names(self):
        """Lấy danh sách tên các gói"""
        packages = self.find_all(self.loc.TV_PACKAGE_NAME)
        return [p.text for p in packages]

    def get_package_descriptions(self):
        """Lấy danh sách mô tả các gói"""
        descs = self.find_all(self.loc.TV_PACKAGE_DESC)
        return [d.text for d in descs]

    def get_package_prices(self):
        """Lấy danh sách giá các gói"""
        prices = self.find_all(self.loc.TV_PRICE)
        return [p.text for p in prices]

    def tap_buy(self):
        """Nhấn nút Mua gói"""
        self.wait_and_tap(self.loc.BTN_BUY)

    def tap_close(self):
        """Đóng màn hình đăng ký"""
        self.wait_and_tap(self.loc.BTN_CLOSE)

    # --------------------------------------------------
    # Chi tiết gói (Plus / Premium)
    # --------------------------------------------------
    def tap_tab_plus(self):
        """Chuyển sang tab gói Plus"""
        self.wait_and_tap(self.loc.TAB_PLUS)

    def tap_tab_premium(self):
        """Chuyển sang tab gói Premium"""
        self.wait_and_tap(self.loc.TAB_PREMIUM)

    def get_package_title(self):
        """Lấy tên gói"""
        return self.get_text(self.loc.TV_TITLE)

    def get_package_subtitle(self):
        """Lấy mô tả ngắn gói"""
        return self.get_text(self.loc.TV_SUBTITLE)

    def get_price(self):
        """Lấy giá gói"""
        return self.get_text(self.loc.TV_PRICE)

    def get_original_price(self):
        """Lấy giá gốc (trước khi giảm)"""
        return self.get_text(self.loc.TV_ORIGINAL_PRICE)

    def get_deal_text(self):
        """Lấy text khuyến mãi"""
        return self.get_text(self.loc.TV_DEAL)

    def get_badge_text(self):
        """Lấy nhãn badge (Plus / Premium)"""
        return self.get_text(self.loc.TV_BADGE)

    def get_bottom_desc(self):
        """Lấy mô tả ở cuối trang"""
        return self.get_text(self.loc.TV_BOTTOM_DESC)

    def tap_buy_cta(self):
        """Nhấn nút CTA mua gói ở cuối trang"""
        self.wait_and_tap(self.loc.BTN_BOTTOM_CTA)
