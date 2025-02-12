import pytest
import allure

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



@allure.title("app.vwo.com Implicit Wait")
@allure.description("Verify that the app.vwo.com is loaded with waits")
def test_negative_tc_app_vwo_com():

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)

    driver.get("https://app.vwo.com/#/login")

    # Implicit Wait
    driver.implicitly_wait(5)

    email_id_webelement = driver.find_element(By.ID,"login-username")
    email_id_webelement.send_keys("admin123@gmail.com")

    password_webelement = driver.find_element(By.ID, "login-password")
    password_webelement.send_keys("Password123")

    sign_in_button = driver.find_element(By.XPATH,"//button[@id='js-login-btn']")
    sign_in_button.click()

