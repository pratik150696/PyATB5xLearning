import time

import pytest
import allure

from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("app.vwo.com Implicit Wait")
@allure.description("Verify that the app.vwo.com is loaded with waits")
def test_negative_tc_app_vwo_com():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)

    driver.get("https://app.vwo.com/#/login")

    email_id_webelement = driver.find_element(By.ID, "login-username")
    email_id_webelement.send_keys("admin123@gmail.com")

    password_webelement = driver.find_element(By.ID, "login-password")
    password_webelement.send_keys("Password123")

    sign_in_button = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    sign_in_button.click()

    ignore_list = [ElementNotVisibleException,ElementNotSelectableException]

    WebDriverWait(driver= driver, poll_frequency=1, timeout=5, ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='js-notification-box-msg']")))

    error_msg_webelement = driver.find_element(By.XPATH, "//div[@id='js-notification-box-msg']")
    print(error_msg_webelement.text)

    assert error_msg_webelement.text == "Your email, password, IP address or location did not match"
