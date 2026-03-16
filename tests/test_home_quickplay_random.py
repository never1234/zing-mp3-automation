import allure
import time
import random
import pytest
from pages.base_page import BasePage
from locators.android_locators import (
    AndroidHomeLocators,
    AndroidPlayerLocators,
    AndroidPlaylistLocators,
)


@allure.feature("Màn hình Khám phá")
class TestHomeQuickPlayRandom:

    @pytest.mark.non_login
    @pytest.mark.free
    @pytest.mark.plus
    @pytest.mark.premium
    @pytest.mark.regression
    @allure.story("Phát nhanh")
    @allure.title("All: Tap ngẫu nhiên item trong section Phát nhanh (lặp 2 lần)")
    def test_quickplay_random_item(self, driver):
        page = BasePage(driver)

        for iteration in range(1, 3):

            with allure.step(f"Lần {iteration} – Bước 1: Tap ngẫu nhiên item trong section 'Phát nhanh'"):
                items = page.find_all(AndroidHomeLocators.QUICK_PLAY_ALL_ITEMS)
                assert len(items) > 0, "Không tìm thấy item nào trong section 'Phát nhanh'"
                random_item = random.choice(items)
                random_item.click()
                time.sleep(2)

            if page.is_visible(AndroidPlaylistLocators.BTN_SHUFFLE):
                # Item là Playlist → màn hình Playlist details đang hiển thị
                with allure.step(f"Lần {iteration} – Bước 2a: Item là Playlist – tap 'Phát ngẫu nhiên'"):
                    page.wait_and_tap(AndroidPlaylistLocators.BTN_SHUFFLE)
                    time.sleep(2)

                with allure.step(f"Lần {iteration} – Bước 2b: Minimize Player"):
                    page.wait_and_tap(AndroidPlayerLocators.MINIMIZE_BTN)
                    time.sleep(1)

                with allure.step(f"Lần {iteration} – Bước 2c: Quay về màn hình Khám phá"):
                    page.wait_and_tap(AndroidHomeLocators.BOTTOM_NAV_HOME)
                    time.sleep(1)

            else:
                # Item là bài hát → Player đang hiển thị trực tiếp
                with allure.step(f"Lần {iteration} – Bước 2: Item là bài hát – minimize Player"):
                    page.wait_and_tap(AndroidPlayerLocators.MINIMIZE_BTN)
                    time.sleep(1)
