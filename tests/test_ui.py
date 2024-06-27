import pytest
from pages.login_page import LoginPage
from pages.books_page import BooksPage
import allure
from selenium.webdriver.common.by import By
from pages.profile_page import ProfilePage
from pages.book_store_page import BookStorePage  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import USER_DATA


@allure.feature('Login')
@allure.story('User Login')
def test_login_user(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    with allure.step("Login existing user"):
        login_page.login(USER_DATA["username"], USER_DATA["password"])
    with allure.step("Verify login success"):
        welcome_message = login_page.find_element((By.ID, "userName-value")).text
        assert "TestUser123" in welcome_message

@allure.feature('Books')
@allure.story('Search Book')
def test_search_book(browser):
    books_page = BooksPage(browser)
    books_page.open_books_page()
    with allure.step("Search for a book"):
        books_page.search_book("Git Pocket Guide")
    with allure.step("Verify search results"):
        results = books_page.get_search_results()
        assert "Git Pocket Guide" in results

@allure.feature('Profile')
@allure.story('Go To Book Store')
def test_go_to_book_store(browser):
    profile_page = ProfilePage(browser)
    book_store_page = BookStorePage(browser)
    profile_page.open_profile_page()
    with allure.step("Click on 'Go To Book Store' button"):
        profile_page.go_to_book_store()
    with allure.step("Verify book store page loaded"):
        assert book_store_page.verify_books_wrapper()




@allure.feature('Books')
@allure.story('Filter Books')
def test_filter_books(browser):
    books_page = BooksPage(browser)
    books_page.open_books_page()
    with allure.step("Filter books by 'Git'"):
        filter_box = books_page.find_element((By.ID, "searchBox"))
        filter_box.send_keys("Git")
    with allure.step("Verify filtered books"):
        results = books_page.get_search_results()
        assert all("Git" in title for title in results)


@allure.feature('Logout')
@allure.story('Logout from Book Store')
def test_logout_from_book_store(browser):
    book_store_page = BookStorePage(browser)
    login_page = LoginPage(browser)
    book_store_page.open_books_page()
    with allure.step("Logout from book store"):
        book_store_page.logout()
    with allure.step("Verify login page loaded"):
        WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "h5"), "Login in Book Store")
        )
        assert "Login in Book Store" in login_page.find_element((By.TAG_NAME, "h5")).text