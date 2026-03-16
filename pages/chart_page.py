from pages.base_page import BasePage
from locators.android_locators import AndroidChartLocators, AndroidChartDetailLocators


class ChartPage(BasePage):
    """Màn hình #ZingChart của Zing MP3"""

    def __init__(self, driver):
        super().__init__(driver)
        self.loc   = AndroidChartLocators if self.platform == "android" else None
        self.loc_d = AndroidChartDetailLocators if self.platform == "android" else None

    # --------------------------------------------------
    # Kiểm tra hiển thị
    # --------------------------------------------------
    def is_chart_visible(self):
        """Kiểm tra màn hình ZingChart đang hiển thị"""
        return self.is_visible(self.loc.ZING_CHART_VIEW) or self.is_visible(self.loc.CHART_SONG_LIST)

    def is_top1_row_visible(self):
        """Kiểm tra hàng bài hát top 1 hiển thị"""
        return self.is_visible(self.loc.CHART_TOP1_ROW)

    # --------------------------------------------------
    # Thông tin chart
    # --------------------------------------------------
    def get_chart_date(self):
        """Lấy ngày giờ cập nhật chart"""
        return self.get_text(self.loc.CHART_DATE_TIME)

    def get_top1_title(self):
        """Lấy tên bài hát top 1"""
        self.wait_for_visible(self.loc.CHART_TOP1_TITLE)
        return self.get_text(self.loc.CHART_TOP1_TITLE)

    def get_top1_artist(self):
        """Lấy tên nghệ sĩ bài hát top 1"""
        return self.get_text(self.loc.CHART_TOP1_ARTIST)

    # --------------------------------------------------
    # Phát nhạc
    # --------------------------------------------------
    def tap_top1_song(self):
        """Nhấn vào bài hát top 1"""
        self.wait_and_tap(self.loc.CHART_TOP1_ROW)

    def tap_fast_play(self):
        """Nhấn nút Phát nhanh"""
        self.wait_and_tap(self.loc.BTN_FAST_PLAY)

    def tap_shuffle(self):
        """Nhấn phát ngẫu nhiên"""
        self.wait_and_tap(self.loc.BTN_SHUFFLE)

    def tap_song_by_rank(self, rank: int):
        """Nhấn vào bài hát theo thứ hạng (1-based)"""
        locator = (
            self.loc.CHART_TOP1_ROW[0],
            self.loc.CHART_TOP1_ROW[1].replace("@text='1'", f"@text='{rank}'")
        )
        self.wait_and_tap(locator)

    # --------------------------------------------------
    # Weekly chart tabs
    # --------------------------------------------------
    def switch_to_vpop(self):
        """Chuyển sang tab V-pop"""
        self.wait_and_tap(self.loc.TAB_VPOP)

    def switch_to_usuk(self):
        """Chuyển sang tab US-UK"""
        self.wait_and_tap(self.loc.TAB_USUK)

    def switch_to_kpop(self):
        """Chuyển sang tab K-pop"""
        self.wait_and_tap(self.loc.TAB_KPOP)

    def get_chart_title(self):
        """Lấy tiêu đề chart weekly"""
        return self.get_text(self.loc.TV_ZING_CHART_TITLE)

    def get_chart_week_text(self):
        """Lấy text tuần của chart"""
        return self.get_text(self.loc.TV_CHART_WEEK)

    def tap_chart_week_btn(self):
        """Nhấn nút chọn tuần chart"""
        self.wait_and_tap(self.loc.BTN_CHART_WEEK)

    # --------------------------------------------------
    # Chart Detail (HCM / HN)
    # --------------------------------------------------
    def is_chart_detail_visible(self):
        """Kiểm tra màn hình chi tiết chart hiển thị"""
        return self.is_visible(self.loc_d.COLLAPSING_TOOLBAR)

    def get_chart_detail_header(self):
        """Lấy tiêu đề chart detail"""
        return self.get_text(self.loc_d.TV_HEADER)

    def tap_chart_detail_shuffle(self):
        """Phát ngẫu nhiên trong chart detail"""
        self.wait_and_tap(self.loc_d.BTN_SHUFFLE)

    def get_chart_detail_top1_title(self):
        """Lấy tên bài hát top 1 trong chart detail"""
        self.wait_for_visible(self.loc_d.SONG_TITLE)
        titles = self.find_all(self.loc_d.SONG_TITLE)
        return titles[0].text if titles else None