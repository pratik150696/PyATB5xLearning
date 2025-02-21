import pytest
import allure
import requests


# pip install pytest allure requests

@allure.title("TC#1 - Verify that 2-2 == 0")
@allure.description("This is a Basic Math Test")
@pytest.mark.smoke
def test_basic_math_test():
    assert 2 - 2 == 0


@allure.title("TC#2 - Verify that 3 - 3 is equal to 0")
@allure.description("This is to verify thst 3-3 is equal to 0")
@pytest.mark.regresssion
def test_sub1():
    assert 3 - 3 == 0


@allure.title("TC#3 - Verify that 1 - 1 is equal to 0")
@allure.description("This is to verify thst 1-1 is equal to 0")
@pytest.mark.smoke
def test_sub1():
    assert 1 - 1 == 0


@pytest.mark.skip(reason = "Not working, skip it")
def test_sub3():
    assert 0 - 0 != 0