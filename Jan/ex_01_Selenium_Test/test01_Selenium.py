import time

from selenium import webdriver
import pytest
import allure

@allure.title("Open the VWO Login")
@pytest.mark.regression
def test_vwo_login():
    driver = webdriver.Edge()
    driver.get("https:/app.vwo.com")
    driver.maximize_window()
    time.sleep(10)