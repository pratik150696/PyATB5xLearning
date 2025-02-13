import time

from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.actions.action_builder import ActionBuilder

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.devtools.v85.input_ import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@allure.title("Action P2")
@allure.description("Verify Mouseback")
def test_verify_action_mouse():

    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    atag = driver.find_element(By.XPATH,"//a[@id='click']")
    atag.click()

    action_builder = ActionBuilder(driver=driver)
    action_builder.pointer_action.pointer_up(MouseButton.BACK)
    # action_builder.perform()   Not work in some window

    time.sleep(10)
