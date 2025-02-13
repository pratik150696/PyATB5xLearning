import allure
from selenium import webdriver
from selenium.common import  NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from allure_commons.types import AttachmentType


@allure.title("Make My Trip Automation")
@allure.description("Verify Make My Trip Automation by using Action Classes")
def test_verify_action_makemytrip():

    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)

    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='commonModal__close']")))


    close_modal = driver.find_element(By.XPATH,"//span[@class='commonModal__close']")
    close_modal.click()



    WebDriverWait(driver =driver,timeout=10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                             ElementNotVisibleException,
                                                                             ElementNotSelectableException]).until(EC.visibility_of_element_located((By.ID,"fromCity")))

    fromcity = driver.find_element(By.ID, "fromCity")
    fromcity.send_keys()

    actions = ActionChains(driver = driver)
    actions.move_to_element(fromcity).click().send_keys("Nag").pause(3).perform()

    time.sleep(2)

    actions.move_to_element(fromcity).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

    allure.attach(driver.get_screenshot_as_png(), name="test_verify_action_makemytrip", attachment_type=AttachmentType.PNG)

    time.sleep(10)
