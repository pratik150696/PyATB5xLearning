import time

from selenium import webdriver

import pytest
import allure


@allure.title("Verify the title of the WebPage")
@pytest.mark.regression
def test_vwo_login():
    driver = webdriver.Chrome()

    driver.get("https:/app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
    time.sleep(10)