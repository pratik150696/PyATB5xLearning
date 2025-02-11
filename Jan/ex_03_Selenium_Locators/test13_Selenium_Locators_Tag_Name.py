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

    all_links_pages = driver.find_elements(By.TAG_NAME, "a")
    print(len(all_links_pages))

    for i in all_links_pages:
        print(i.text)

        if "Start a free trial" in i.text:
            i.click()
            break

    time.sleep(3)
    driver.quit()