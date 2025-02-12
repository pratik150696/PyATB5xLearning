import time

import pytest
import allure

from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Modal")
@allure.description("Handle Modal")
def test_modal():
    driver = webdriver.Chrome()

    driver.get("https://www.makemytrip.com/")

    WebDriverWait(driver=driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//section[@class='modalMain tcnFooter']")))

    close_modal = driver.find_element(By.XPATH,"//span[@class='commonModal__close']")
    close_modal.click()

    time.sleep(5)