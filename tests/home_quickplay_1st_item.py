import allure
import pytest
from pages.base_page import BasePage
from locators.android_locators import (
    AndroidHomeLocators,
    AndroidPlayerLocators,
    AndroidPlaylistLocators,
)


@allure.feature("Màn hình Khám phá")
class TestHomeQuickPlay:

    @pytest.mark.non_login
    @pytest.mark.free
    @pytest.mark.plus
    @pytest.mark.premium
    @pytest.mark.regression
    @allure.story("Phát nhanh")
    @allure.title("All: Tap item đầu tiên trong section Phát nhanh")
    def test_quickplay_first_item(self, driver):
        page = BasePage(driver)

        with allure.step("Bước 1: Tap item đầu tiên trong section 'Phát nhanh'"):
            page.wait_and_tap(AndroidHomeLocators.QUICK_PLAY_FIRST_ITEM)

        if page.is_visible(AndroidPlaylistLocators.BTN_SHUFFLE):
            # Item là Playlist → màn hình Playlist details đang hiển thị
            with allure.step("Bước 2: Item là Playlist – tap 'Phát ngẫu nhiên'"):
                page.wait_and_tap(AndroidPlaylistLocators.BTN_SHUFFLE)

            with allure.step("Bước 3: Minimize Player"):
                page.wait_and_tap(AndroidPlayerLocators.MINIMIZE_BTN)

            with allure.step("Bước 4: Quay về màn hình Khám phá"):
                page.wait_and_tap(AndroidHomeLocators.BOTTOM_NAV_HOME)

        else:
            # Item là bài hát → Player đang hiển thị trực tiếp
            with allure.step("Bước 2: Item là bài hát – minimize Player"):
                page.wait_and_tap(AndroidPlayerLocators.MINIMIZE_BTN)
