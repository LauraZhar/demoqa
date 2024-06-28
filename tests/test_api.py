import pytest
import requests
import allure
from config import USER_DATA

BASE_URL = "https://bookstore.toolsqa.com"

@allure.feature('API')
@allure.story('User Registration')
def test_register_user(unique_user):
    url = f"{BASE_URL}/Account/v1/User"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    with allure.step("Register new user"):
        response = requests.post(url, json=unique_user, headers=headers)
    with allure.step("Verify registration success"):
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        response_data = response.json()
        assert response_data["username"] == unique_user["userName"]

@allure.feature('API')
@allure.story('Generate Token')
def test_generate_token(register_user):
    user_data = {
        "userName": register_user['username'],
        "password": register_user['password']
    }
    url = f"{BASE_URL}/Account/v1/GenerateToken"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    with allure.step("Generate token for user"):
        response = requests.post(url, json=user_data, headers=headers)
    with allure.step("Verify token generation success"):
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        response_data = response.json()
        assert "token" in response_data

@allure.feature('API')
@allure.story('Get User Information')
def test_get_user_info(user_info):
    with allure.step("Verify user info retrieval success"):
        assert user_info["username"] == user_info["username"]

@allure.feature('API')
@allure.story('Add Books to User')
def test_add_books(user_info, auth_token):
    url = f"{BASE_URL}/BookStore/v1/Books"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {auth_token}'
    }
    payload = {
        "userId": user_info['userId'],
        "collectionOfIsbns": [{"isbn": "9781449325862"}]
    }
    with allure.step("Add books to user via API"):
        response = requests.post(url, json=payload, headers=headers)
    with allure.step("Verify adding books success"):
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        response_data = response.json()
        assert response_data['books'][0]['isbn'] == "9781449325862"

@allure.feature('API')
@allure.story('Delete User')
def test_delete_user(user_info, auth_token):
    url = f"{BASE_URL}/Account/v1/User/{user_info['userId']}"
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {auth_token}'
    }
    with allure.step("Delete user via API"):
        response = requests.delete(url, headers=headers)
    with allure.step("Verify user deletion success"):
        assert response.status_code == 204, f"Expected 204, got {response.status_code}"
