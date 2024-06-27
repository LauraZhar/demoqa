
from selenium.webdriver.common.by import By
from .base_page import BasePage

class BooksPage(BasePage):
    BOOKS_URL = "/books"
    SEARCH_BOX = (By.ID, "searchBox")
    SEARCH_BUTTON = (By.ID, "basic-addon2")
    BOOK_TITLE = (By.CLASS_NAME, "mr-2")

    def open_books_page(self):
        self.open(self.BOOKS_URL)

    def search_book(self, book_title):
        self.find_element(self.SEARCH_BOX).send_keys(book_title)
        self.find_element(self.SEARCH_BUTTON).click()

    def get_search_results(self):
        return [book.text for book in self.find_elements(self.BOOK_TITLE)]
