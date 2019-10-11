from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.input_field import InputField


class SignInMenu:
    input_login_field_loc = "//input[@type='email']"
    input_password_field_loc = "//input[@type='password']"
    submit_button_loc = "//button[@data-at-selector='welcomeSignInBtn']"

    def log_in(self, login, password):
        self.get_login_field().send_keys(login)
        self.get_password_filed().send_keys(password)
        self.get_submit_button().click()

    def get_submit_button(self):
        return Button(By.XPATH, self.submit_button_loc, "Submit login and password button")

    def get_login_field(self):
        return InputField(By.XPATH, self.input_login_field_loc, "Field for input login")

    def get_password_filed(self):
        return InputField(By.XPATH, self.input_password_field_loc, "Field for input password")
