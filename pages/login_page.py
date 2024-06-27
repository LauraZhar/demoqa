
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    LOGIN_URL = "/login"
    USERNAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")

    def open_login_page(self):
        self.open(self.LOGIN_URL)

    def login(self, username, password):
        self.find_element(self.USERNAME_INPUT).send_keys(username)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        self.find_element(self.LOGIN_BUTTON).click()
