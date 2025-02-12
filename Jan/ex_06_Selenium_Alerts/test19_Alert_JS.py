import time

import pytest
import allure

from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Alert")
@allure.description("Verify Alert")
def test_alert_js_normal():
    driver = webdriver.Chrome()

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    element_prompt.click()

    WebDriverWait(driver=driver, timeout= 5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()

    verify_msg = driver.find_element(By.XPATH,"//p[@id='result']")
    print(verify_msg.text)

    assert verify_msg.text == "You successfully clicked an alert"

    time.sleep(5)

def test_alert_confirm():
    driver = webdriver.Chrome()

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_confirm = driver.find_element(By.XPATH, "//button[@onclick = 'jsConfirm()']")
    element_confirm.click()

    WebDriverWait(driver =driver,timeout=3).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.dismiss()

    cancel_msg = driver.find_element(By.XPATH, "//p[@id='result']")
    print(cancel_msg.text)

    assert cancel_msg.text == "You clicked: Cancel"

    time.sleep(5)

def test_alert_prompt():
    driver = webdriver.Chrome()

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    element_prompt.click()

    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.send_keys("Pratik")
    alert.accept()

    result_text = driver.find_element(By.XPATH,"//p[@id='result']")
    print(result_text.text)

    assert result_text.text == "You entered: Pratik"

    time.sleep(5)


