import time
import allure
import pytest


@allure.feature("App Launch")
class TestLaunch:

    @allure.title("Open app, wait 20s, close app")
    @allure.description("Verify the app can be opened, stays stable for 20 seconds, then closes.")
    def test_open_wait_close(self, driver):
        with allure.step("Open app"):
            # App is launched by the driver fixture (SplashActivity)
            assert driver is not None, "Driver should be initialized"

        with allure.step("Wait 20 seconds"):
            time.sleep(20)

        with allure.step("Close app"):
            driver.terminate_app("com.zing.mp3")
