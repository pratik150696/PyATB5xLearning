import time

from selenium import webdriver

import pytest
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_katalon_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--window-size=500,300")
    # chrome_options.add_argument("--headless")


    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")


    # Step 1:  Identify Element
    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")

    # Step 2: Perform click action
    make_appointment_element.click()

    # Step 3: Verify Element
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    # Step 4: Wait & Maximize
    time.sleep(5)

    # Step 5: Close
    driver.quit()

