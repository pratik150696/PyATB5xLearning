import time

from selenium import webdriver

import pytest
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
import os


@allure.title("VWO Login Negative TC")
@allure.description("TC1: VWO Login with invalid id and password")
def test_vwo_chrome():
    driver = webdriver.Chrome()
    # Enter URL
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_app_button = driver.find_element(By.XPATH, "//a[@id ='btn-make-appointment']")
    make_app_button.click()

    time.sleep(5)
    driver.quit()