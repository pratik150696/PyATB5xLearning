from selenium import webdriver

import pytest
import allure

from selenium.webdriver.common.by import By


@allure.title("Open Desktop Computer and print value")
@allure.description("Verify that 62 items are there in Mac mini")
def test_desktop_comp():
    driver = webdriver.Chrome()

    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    search_input_webelement = driver.find_element(By.XPATH, "//input[@title ='Search']")
    search_input_webelement.send_keys("Macmini")

    search_button_webelement = driver.find_element(By.ID, "gh-search-btn")
    search_button_webelement.click()

    list_titles = driver.find_elements(By.XPATH, "//div[@class='s-item__title']")

    list_prices = driver.find_elements(By.XPATH,"//div//span[@class ='s-item__price']")


    for items in list_titles:
        print(items.text)

    for items_price in list_prices:
        print(items_price.text)



