from selenium import webdriver

import pytest
import allure


@allure.title("Open the VWO App")
@pytest.mark.regression
def test_vwo_login():
    driver = webdriver.Chrome()
    # 1. This code is translated into the API Request
    # 2. Post Request ---> browserDriver(Server)
    # 3. Session ID 16 digit will be created

    driver.get("https:/app.vwo.com")
    print(driver.title)
    print(driver.page_source)
    print(driver.current_url)
