import pytest
import allure
import requests


@allure.title("Verify the GET Request of Restful Booker")
@allure.description("This test case check booking 1 and Verify the Response")
@pytest.mark.positive
def test_get_request_positive():
    URL = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=URL)
    # print(response_data.text)
    assert response_data.status_code == 200


@allure.title("Verify the GET Request of Restful Booker with invalid Id")
@allure.description("This test case check booking -1 and Verify the Response")
@pytest.mark.negative
def test_get_request_negative():
    URL = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=URL)
    assert response_data.status_code == 404
