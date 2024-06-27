from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProfilePage(BasePage):
    PROFILE_URL = "/profile"
    GO_TO_STORE_BUTTON = (By.ID, "gotoStore")

    def open_profile_page(self):
        self.open(self.PROFILE_URL)

    def go_to_book_store(self):
        # Использование JavaScript для клика по кнопке
        self.driver.execute_script("arguments[0].click();", self.find_element(self.GO_TO_STORE_BUTTON))
