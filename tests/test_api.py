import pytest
import requests
import allure

BASE_URL = "https://bookstore.toolsqa.com"
USER_DATA = {}
TOKEN = ""

@allure.feature('API')
@allure.story('User Registration')
def test_register_user(unique_username):
    global USER_DATA
    url = f"{BASE_URL}/Account/v1/User"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload = {"userName": unique_username, "password": "Test@1234"}
    with allure.step("Register new user via API"):
        response = requests.post(url, json=payload, headers=headers)
    with allure.step("Verify registration success"):
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        USER_DATA = {"username": unique_username, "userID": response.json()["userID"], "password": "Test@1234"}

@allure.feature('API')
@allure.story('User Authentication')
def test_generate_token():
    global TOKEN
    url = f"{BASE_URL}/Account/v1/GenerateToken"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload = {"userName": USER_DATA["username"], "password": USER_DATA["password"]}
    with allure.step("Generate token via API"):
        response = requests.post(url, json=payload, headers=headers)
    with allure.step("Verify token generation success"):
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        TOKEN = response.json()["token"]

@allure.feature('API')
@allure.story('Get User Information')
def test_get_user_info():
    global TOKEN
    url = f"{BASE_URL}/Account/v1/User/{USER_DATA['userID']}"
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {TOKEN}'
    }
    with allure.step("Get user info via API"):
        response = requests.get(url, headers=headers)
    with allure.step("Verify user info retrieval success"):
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json().get("username") == USER_DATA["username"]

@allure.feature('API')
@allure.story('Add Books to Collection')
def test_add_books():
    global TOKEN
    url = f"{BASE_URL}/BookStore/v1/Books"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {TOKEN}'
    }
    payload = {
        "userId": USER_DATA["userID"],
        "collectionOfIsbns": [{"isbn": "9781449325862"}, {"isbn": "9781449331818"}]
    }
    with allure.step("Add books to user collection via API"):
        response = requests.post(url, json=payload, headers=headers)
    with allure.step("Verify books addition success"):
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        assert len(response.json()["books"]) == 2



@allure.feature('API')
@allure.story('Get Book Information')
def test_get_book_info():
    global TOKEN
    url = f"{BASE_URL}/BookStore/v1/Book?ISBN=9781449325862"
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {TOKEN}'
    }
    with allure.step("Get book info via API"):
        response = requests.get(url, headers=headers)
    with allure.step("Verify book info retrieval success"):
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json().get("isbn") == "9781449325862"

@allure.feature('API')
@allure.story('Delete User')
def test_delete_user():
    global TOKEN
    url = f"{BASE_URL}/Account/v1/User/{USER_DATA['userID']}"
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {TOKEN}'
    }
    with allure.step("Delete user via API"):
        response = requests.delete(url, headers=headers)
    with allure.step("Verify user deletion success"):
        assert response.status_code == 204, f"Expected 204, got {response.status_code}"