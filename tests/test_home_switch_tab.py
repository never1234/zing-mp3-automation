import allure
import pytest
from pages.base_page import BasePage
from locators.android_locators import AndroidHomeLocators


@allure.feature("Màn hình Khám phá")
class TestHomeSwitchTab:

    @pytest.mark.free
    @pytest.mark.plus
    @pytest.mark.premium
    @pytest.mark.regression
    @allure.story("Category Tabs")
    @allure.title("Free/Plus/Premium: Chuyển đổi tab danh mục trên màn hình Khám phá")
    def test_switch_category_tabs(self, driver):
        page = BasePage(driver)

        with allure.step("Bước 1: Chuyển sang tab Tập trung"):
            page.wait_and_tap(AndroidHomeLocators.TAB_TAP_TRUNG)

        with allure.step("Bước 2: Chuyển sang tab Thư giãn"):
            page.wait_and_tap(AndroidHomeLocators.TAB_THU_GIAN)

        with allure.step("Bước 3: Chuyển sang tab Workout"):
            page.wait_and_tap(AndroidHomeLocators.TAB_WORKOUT)

        with allure.step("Bước 4: Chuyển sang tab Cho bạn"):
            page.wait_and_tap(AndroidHomeLocators.TAB_CHO_BAN)

        with allure.step("Bước 5: Chuyển sang tab Thư giãn"):
            page.wait_and_tap(AndroidHomeLocators.TAB_THU_GIAN)

        with allure.step("Bước 6: Chuyển sang tab Cho bạn"):
            page.wait_and_tap(AndroidHomeLocators.TAB_CHO_BAN)

        with allure.step("Bước 7: Chuyển sang tab Tập trung"):
            page.wait_and_tap(AndroidHomeLocators.TAB_TAP_TRUNG)

        with allure.step("Bước 8: Chuyển sang tab Cho bạn"):
            page.wait_and_tap(AndroidHomeLocators.TAB_CHO_BAN)
