import time

from selenium import webdriver

import pytest
import allure


@allure.title("Verify the title of the WebPage")
def test_katalon_login():
    driver = webdriver.Chrome()

    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "PURA Healthcare Service" in driver.page_source:
        print("Text Found !!, Test Case Passed!")
    else:
        print("Text not found on WebPage")
        pytest.fail("Text not found on WebPage")
