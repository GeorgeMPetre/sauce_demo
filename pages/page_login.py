from selenium.common import NoSuchElementException

from utils.base_page import BasePage
from pages.locators.locators import LoginPageLocators


class LoginPage(BasePage):
    def enter_username(self, username):
        self.enter_text(LoginPageLocators.USERNAME_INPUT, username)


    def enter_password(self, password):
        self.enter_text(LoginPageLocators.PASSWORD_INPUT, password)


    def click_login(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)



    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        try:
            return self.driver.find_element(*LoginPageLocators.ERROR_MESSAGE).text
        except NoSuchElementException:
            return ""


    
