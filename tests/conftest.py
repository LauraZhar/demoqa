import pytest
import requests
import time
from config import USER_DATA

BASE_URL = "https://bookstore.toolsqa.com"

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def unique_user():
    timestamp = str(int(time.time()))
    user_data = {
        "userName": f"TestUser_{timestamp}",
        "password": "Test@1234"
    }
    return user_data

@pytest.fixture(scope="function")
def register_user(unique_user):
    url = f"{BASE_URL}/Account/v1/User"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=unique_user, headers=headers)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    return {"username": unique_user["userName"], "password": unique_user["password"], "userId": response.json()['userID'] }

@pytest.fixture(scope="function")
def auth_token(register_user):
    user_data = {
        "userName": register_user['username'],
        "password": register_user['password']
    }
    url = f"{BASE_URL}/Account/v1/GenerateToken"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=user_data, headers=headers)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    return response.json()["token"]

@pytest.fixture(scope="function")
def user_info(register_user, auth_token):
   
    url = f"{BASE_URL}/Account/v1/User/{register_user['userId']}"
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {auth_token}'
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    return response.json()
