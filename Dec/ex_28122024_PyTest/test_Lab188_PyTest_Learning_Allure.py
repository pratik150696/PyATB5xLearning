import pytest
import allure

@allure.title("Verify that the create booking with valid data is working")
@allure.description("This testcase check for the positive create booking")
@pytest.mark.positive
def test_create_booking_positive():
    print("Test1")
    assert 1-1 == 2

@allure.title("Verify that the create booking with invalid data is working")
@allure.description("This testcase check for the negative create booking")
@pytest.mark.negative
def test_create_booking_negative1():
    print("Test2")
    assert 1+1 == 2

@allure.title("Verify that the create booking with invalid data is working")
@allure.description("This testcase check for the negative create booking")
@pytest.mark.negative
def test_create_booking_negative2():
    print("Test3")
    assert 1+1 == 2