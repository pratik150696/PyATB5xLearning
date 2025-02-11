import time

from selenium import webdriver

import pytest
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os


@allure.title("VWO SignUp")
@allure.description("Click on sign up button and verify url")
def test_vwo_signup_button():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))

    startTrial_webelement = driver.find_element(By.LINK_TEXT,"Start a free trial")
    startTrial_webelement.click()

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    time.sleep(3)
    driver.quit()




