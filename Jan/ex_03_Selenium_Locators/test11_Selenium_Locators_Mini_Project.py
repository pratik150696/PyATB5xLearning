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
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")


    driver = webdriver.Chrome(chrome_options)

    # Enter URL
    driver.get(os.getenv("URL"))

    # Enter Login Id & Password
    email_webelement = driver.find_element(By.NAME, "username")
    email_webelement.send_keys(os.getenv("INVALID_USERNAME"))

    password_webelement = driver.find_element(By.ID, "login-password")
    password_webelement.send_keys(os.getenv("INVALID_PASSWORD"))

    submit_button_webelement = driver.find_element(By.ID,"js-login-btn")
    submit_button_webelement.click()

    time.sleep(3)

    error_msg = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg.text)

    assert error_msg.text == os.getenv("error_msg_expected")

