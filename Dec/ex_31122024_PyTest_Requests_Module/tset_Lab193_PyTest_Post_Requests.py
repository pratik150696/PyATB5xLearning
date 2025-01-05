import pytest
import allure
import requests

# Create Token POST
base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}

def get_token():
    base_path = "/auth"
    full_url = base_url + base_path

    json_payload_auth = {
        "username": "admin",
        "password": "password123"
    }

    response_data = requests.post(url = full_url, headers=headers, json= json_payload_auth)
    assert response_data.status_code == 200

    response_data_json = response_data.json()
    token = response_data_json["token"]
    print(token)
    print(len(token))

    assert type(token) == str
    assert len(token) > 0
    return token

def get_booking_id():
    base_path = "/booking"
    full_url = base_url+base_path

    json_payload = {
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

    response_data = requests.post(url = full_url, headers= headers, json = json_payload)
    response_data_json = response_data.json()
    booking_id = response_data_json["bookingid"]
    return booking_id

def test_put_requests():
    token = get_token()
    booking_id = get_booking_id()
    print(token)
    print(booking_id)

    base_path = "/booking" + str(booking_id)
    full_url = base_url + base_path
    cookie = "token=" + token
