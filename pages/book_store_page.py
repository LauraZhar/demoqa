from selenium.webdriver.common.by import By
from .base_page import BasePage

class BookStorePage(BasePage):
    BOOKS_WRAPPER = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.books-wrapper > div.ReactTable.-striped.-highlight")
    LOGOUT_BUTTON = (By.ID, "submit")
    LOGIN_HEADER = (By.TAG_NAME, "h5")

    def open_books_page(self):
        self.open("/books")

    def logout(self):
        self.find_element(self.LOGOUT_BUTTON).click()

    def verify_books_wrapper(self):
        return self.find_element(self.BOOKS_WRAPPER)

    def verify_login_header(self):
        return self.find_element(self.LOGIN_HEADER)
