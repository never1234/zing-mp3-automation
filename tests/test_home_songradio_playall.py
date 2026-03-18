import allure
import time
import pytest
from pages.base_page import BasePage
from locators.android_locators import (
    AndroidHomeLocators,
    AndroidPlayerLocators,
)


@allure.feature("Màn hình Khám phá")
class TestHomeSongRadioPlayAll:

    @pytest.mark.free
    @pytest.mark.plus
    @pytest.mark.premium
    @pytest.mark.regression
    @allure.story("Gợi ý bài hát")
    @allure.title("Free/Plus/Premium: Phát tất cả section Gợi ý bài hát, refresh rồi phát lại và pause")
    def test_songradio_playall(self, driver):
        page = BasePage(driver)

        with allure.step("Bước 1: Tap 'Phát tất cả' tại section 'Gợi ý bài hát'"):
            page.wait_and_tap(AndroidHomeLocators.BTN_PHAT_TAT_CA)
            time.sleep(2)

        with allure.step("Bước 2: Minimize Player"):
            page.minimize_player()
            time.sleep(1)

        with allure.step("Bước 3: Tap nút Refresh tại section 'Gợi ý bài hát'"):
            page.scroll_and_tap(AndroidHomeLocators.BTN_REFRESH)
            time.sleep(2)

        with allure.step("Bước 4: Tap 'Phát tất cả' tại section 'Gợi ý bài hát' lần 2"):
            page.scroll_and_tap(AndroidHomeLocators.BTN_PHAT_TAT_CA)
            time.sleep(2)

        with allure.step("Bước 5: Tap nút Pause trên màn hình Player"):
            page.wait_and_tap(AndroidPlayerLocators.PLAY_PAUSE_BTN)
            time.sleep(1)
