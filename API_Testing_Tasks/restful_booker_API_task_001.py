import numbers

import pytest
import allure
import requests


def create_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    header = {
        "content-type" : "application/json",
        "Accept" : "application/json"
    }
    req_body = {
    "firstname" : "Ashwin",
    "lastname" : "Jadeja",
    "totalprice" : 500,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2024-04-01",
        "checkout" : "2024-04-06"
    },
    "additionalneeds" : "Dinner"
    }
    response = requests.post(url=url, headers=header, json=req_body)
    resp_body = response.json()
    return resp_body["bookingid"]

def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"content-type":"application/json"}
    req_body = {
        "username" : "admin",
        "password" : "password123"
    }
    response = requests.post(url=url, headers=headers, json=req_body)
    body = response.json()
    token_1 = body["token"]
    return token_1
@pytest.mark.test_001_group
def test_tc001_create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"content-type":"application/json"}
    req_body = {
        "username" : "admin",
        "password" : "password123"
    }
    response = requests.post(url=url, headers=headers, json=req_body)
    body = response.json()
    token_1 = body["token"]
    print(token_1)
    assert response.status_code == 200
    assert isinstance(token_1, str)

@pytest.mark.test_001_group
def test_tc002_get_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    response = requests.get(url=url)
    resp_data = response.json()
    booking_id = resp_data[0]["bookingid"]
    assert response.status_code == 200
    assert isinstance(booking_id, int)

@pytest.mark.test_001_group
def test_tc003_get_one_booking():
    url = "https://restful-booker.herokuapp.com/booking/"
    param = 32
    fullpath = url + str(param)
    headers = {"Accept": "application/json"}
    response = requests.get(url=fullpath,headers=headers)
    body = response.json()
    print()
    print(body)
    assert body['depositpaid']

@pytest.mark.test_001_group
def test_tc004_create_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    header = {
        "content-type": "application/json",
        "Accept": "application/json"
    }
    req_body = {
        "firstname": "Ashwin",
        "lastname": "Jadeja",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-01",
            "checkout": "2024-04-06"
        },
        "additionalneeds": "Dinner"
    }
    response = requests.post(url=url, headers=header, json=req_body)
    resp_body = response.json()
    print(resp_body)
    assert response.status_code == 200
    assert resp_body['booking']['firstname'] == "Ashwin"

@pytest.mark.test_001_group
def test_tc005_full_Update_booking():
    url = "https://restful-booker.herokuapp.com/booking/"
    id = create_booking()
    fullpath = url + str(id)
    cookie_ele = "token=" + create_token()
    headers = {
        "content-type" : "application/json",
        "Accept" : "application/json",
        "cookie" : cookie_ele
    }
    req_body = {
        "firstname": "Gill",
        "lastname": "Pant",
        "totalprice": 287,
        "depositpaid": True,
        "bookingdates": {
            "checkin" : "2024-04-05",
            "checkout" : "2024-04-09"
        },
        "additionalneeds": "Lunch"
    }
    response = requests.put(url=fullpath, headers=headers, json=req_body)
    resp_body = response.json()
    assert response.status_code == 200
    assert resp_body["firstname"] == "Gill"
    assert resp_body["additionalneeds"] == "Lunch"

@pytest.mark.test_001_group
def test_tc006_partial_Update_booking():
    url = "https://restful-booker.herokuapp.com/booking/"
    id = create_booking()
    fullpath = url + str(id)
    cookie_ele = "token=" + create_token()
    headers = {
        "content-type": "application/json",
        "Accept": "application/json",
        "cookie": cookie_ele
    }
    req_body = {
        "firstname": "Darryl",
        "lastname": "Pandey"
    }
    response = requests.patch(url=fullpath, headers=headers, json=req_body)
    resp_body = response.json()
    assert response.status_code == 200
    assert resp_body["firstname"] == "Darryl"
    assert resp_body["lastname"] == "Pandey"

@pytest.mark.test_001_group
def test_tc007_delete_booking():
    url = "https://restful-booker.herokuapp.com/booking/"
    id = create_booking()
    fullpath = url + str(id)
    cookie_ele = "token=" + create_token()
    headers = {
        "content-type": "application/json",
        "cookie": cookie_ele
    }
    response = requests.delete(url=fullpath, headers=headers)
    assert response.status_code == 201
