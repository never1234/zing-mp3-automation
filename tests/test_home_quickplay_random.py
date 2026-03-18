import allure
import time
import random
import pytest
from pages.base_page import BasePage
from locators.android_locators import (
    AndroidHomeLocators,
    AndroidChartLocators,
)


@allure.feature("Màn hình Khám phá")
class TestHomeQuickPlayRandom:

    @pytest.mark.non_login
    @pytest.mark.free
    @pytest.mark.plus
    @pytest.mark.premium
    @pytest.mark.regression
    @allure.story("Phát nhanh")
    @allure.title("All: Tap ngẫu nhiên item trong section Phát nhanh → điều hướng đến ZingChart (lặp 2 lần)")
    def test_quickplay_random_item(self, driver):
        page = BasePage(driver)

        for iteration in range(1, 3):

            with allure.step(f"Lần {iteration} – Bước 1: Tap ngẫu nhiên item trong section 'Phát nhanh'"):
                items = page.find_all(AndroidHomeLocators.QUICK_PLAY_ALL_ITEMS)
                assert len(items) > 0, "Không tìm thấy item nào trong section 'Phát nhanh'"
                random_item = random.choice(items)
                random_item.click()
                time.sleep(2)

            with allure.step(f"Lần {iteration} – Bước 2: Kiểm tra điều hướng đến màn hình ZingChart"):
                assert page.is_visible(AndroidChartLocators.ZING_CHART_VIEW) or \
                       page.is_visible(AndroidChartLocators.CHART_DATE_TIME), \
                    "Màn hình ZingChart không hiển thị sau khi tap item 'Phát nhanh'"

            with allure.step(f"Lần {iteration} – Bước 3: Quay về màn hình Khám phá"):
                page.wait_and_tap(AndroidHomeLocators.BOTTOM_NAV_HOME)
                time.sleep(1)
