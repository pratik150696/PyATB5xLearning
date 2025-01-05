import pytest
import allure
import requests


# Create Booking POST

@allure.title("TC#1 - Create Booking CRUD Positive")
@allure.description("Verify the create booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path_post = "/booking"

    full_url = base_url + base_path_post

    headers = {
        "content-Type": "application/json"
    }

    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url=full_url, headers=headers, json=payload)

    # Status code verification
    assert response_data.status_code == 200

    # BookingID > 0, firstname == Jim
    response_data_json = response_data.json()
    booking_id = response_data_json["bookingid"]
    print(booking_id)
    assert booking_id > 0
    assert booking_id is not None
    assert type(booking_id) == int

    firstname = response_data_json["booking"]["firstname"]
    print(firstname)

    assert firstname == "Jim"
    assert type(firstname) == str

    lastname = response_data_json["booking"]["lastname"]
    totalprice = response_data_json["booking"]["totalprice"]
    deposit_paid = response_data_json["booking"]["depositpaid"]

    print(lastname, totalprice, deposit_paid)

    assert lastname == "Brown"
    assert totalprice == 111
    assert deposit_paid == True

    checkin = response_data_json["booking"]["bookingdates"]["checkin"]
    checkout = response_data_json["booking"]["bookingdates"]["checkout"]

    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

    time = response_data.elapsed.total_seconds()
    assert time < 5


@allure.title("TC#2 - Create Booking CRUD Negative")
@allure.description("Verify that invalid payload/ No payload booking is not created!")
@pytest.mark.crud
def test_create_booking_negative_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path_post = "/booking"

    URL = base_url + base_path_post

    headers = {"Content-Type": "application/json"}
    json_payload = {}

    response = requests.post(url=URL, headers=headers, json=json_payload)
    assert response.status_code == 500
    print(response.text)
    assert response.text == "Internal Server Error"
