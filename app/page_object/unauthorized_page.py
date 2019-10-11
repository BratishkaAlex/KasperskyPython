from selenium.webdriver.common.by import By

from app.app_forms.sign_in_menu import SignInMenu
from framework.elements.button import Button


class UnauthorizedPage:
    sign_in_button_loc = "//div[@class='signin-invite']//button[contains(@class,'js-signin-button')]"

    def __init__(self):
        self.__sign_in_menu = SignInMenu()

    def get_sign_in_button(self):
        return Button(By.XPATH, self.sign_in_button_loc, "Sign in button")

    def sign_in(self):
        self.get_sign_in_button().click()

    @property
    def sign_in_menu(self):
        return self.__sign_in_menu
