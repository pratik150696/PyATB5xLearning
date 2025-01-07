import pytest
import requests
from dotenv import load_dotenv
import os


@pytest.fixture()
def create_token():
    load_dotenv()
    username = os.getenv("EMAILID")
    password = os.getenv("PASSWORD")
    print(username,password)
    print("Creating Token......")

    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type" : "application/json"}
    json_payload = {
        "username" : username,
        "password" : password
    }

    response_data = requests.post(url = url, headers= headers, json=json_payload)
    response_data_json = response_data.json()
    token = response_data_json["token"]
    return token


@pytest.fixture()
def create_booking_id():
    print("Creating Booking Id...............")

    url = "https://restful-booker.herokuapp.com/booking"
    headers = {
        "Content-Type" : "application/json"
    }
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


    response_data = requests.post(url=url, headers=headers,json=json_payload)
    response_data_json = response_data.json()
    booking_id = response_data_json["bookingid"]
    return booking_id




