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
def test_login_user(browser, register_user):
    login_page = LoginPage(browser)
    login_page.open_login_page()   
    
     # Прокрутка страницы вниз
    with allure.step("Scroll down to avoid ads"):
        browser.execute_script("window.scrollTo(200, document.body.scrollHeight);")

    with allure.step("Login existing user"):
        login_page.login(register_user["username"], register_user["password"])
    

    
    with allure.step("Verify login success"):
        welcome_message_element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "userName-value"))
        )
        assert register_user["username"] in welcome_message_element.text

@allure.feature('Books')
@allure.story('Search Book')
def test_search_book(browser, register_user):
    login_page = LoginPage(browser)
    login_page.open_login_page()
# Прокрутка страницы вниз
    with allure.step("Scroll down to avoid ads"):
        browser.execute_script("window.scrollTo(200, document.body.scrollHeight);")

    login_page.login(register_user["username"], register_user["password"])
    
    books_page = BooksPage(browser)
    books_page.open_books_page()


    with allure.step("Search for a book"):
        books_page.search_book("Git Pocket Guide")
    
    with allure.step("Verify search results"):
        book_selector = (By.CSS_SELECTOR, "#see-book-Git\\ Pocket\\ Guide > a")
        book_element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(book_selector)
        )
        assert "Git Pocket Guide" in book_element.text

@allure.feature('Profile')
@allure.story('Go To Book Store')
def test_go_to_book_store(browser, register_user):
    login_page = LoginPage(browser)
    login_page.open_login_page()

    # Прокрутка страницы вниз
    with allure.step("Scroll down to avoid ads"):
        browser.execute_script("window.scrollTo(200, document.body.scrollHeight);")

    login_page.login(register_user["username"], register_user["password"])
    
    # Добавляем ожидание успешного входа
    with allure.step("Verify login success"):
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "userName-value"))
        )
    
    profile_page = ProfilePage(browser)
    book_store_page = BookStorePage(browser)
    profile_page.open_profile_page()
    
    with allure.step("Click on 'Go To Book Store' button"):
        profile_page.go_to_book_store()
    
    with allure.step("Verify book store page loaded"):
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".books-wrapper .ReactTable"))
        )

import pytest
from pages.login_page import LoginPage
from pages.books_page import BooksPage
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature('Books')
@allure.story('Filter Books')
def test_filter_books(browser, register_user):
    login_page = LoginPage(browser)
    login_page.open_login_page()
# Прокрутка страницы вниз
    with allure.step("Scroll down to avoid ads"):
        browser.execute_script("window.scrollTo(200, document.body.scrollHeight);")

    login_page.login(register_user["username"], register_user["password"])
    
    books_page = BooksPage(browser)
    books_page.open_books_page()
    
    with allure.step("Filter books by 'Git'"):
        filter_box = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "searchBox"))
        )
        filter_box.send_keys("Git")
    

@allure.feature('Logout')
@allure.story('Logout from Book Store')
def test_logout_from_book_store(browser, register_user):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    # Прокрутка страницы вниз
    with allure.step("Scroll down to avoid ads"):
        browser.execute_script("window.scrollTo(200, document.body.scrollHeight);")
        
    login_page.login(register_user["username"], register_user["password"])
    
    # Добавляем ожидание успешного входа
    with allure.step("Verify login success"):
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "userName-value"))
        )
    
    book_store_page = BookStorePage(browser)
    
    with allure.step("Logout from book store"):
        logout_button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "submit"))
        )
        # Скроллинг к элементу и использование JavaScript для клика
        browser.execute_script("arguments[0].scrollIntoView(true);", logout_button)
        browser.execute_script("arguments[0].click();", logout_button)
    
    with allure.step("Verify login page loaded"):
        WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "h5"), "Login in Book Store")
        )
        assert "Login in Book Store" in login_page.find_element((By.TAG_NAME, "h5")).text
