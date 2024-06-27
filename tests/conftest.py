import pytest
from selenium import webdriver
import allure
import uuid
import requests

BASE_URL = "https://bookstore.toolsqa.com"

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def unique_username():
    return f"user_{uuid.uuid4().hex[:8]}"
