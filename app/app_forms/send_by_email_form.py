from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.input_field import InputField
from framework.utils.waiter import Waiter


class SendByEmailForm:
    input_login_field_loc_pattern = "//input[@id='Email' and @value='%s']"
    submit_button_loc = "//button[@data-at-selector='installerSendSelfBtn']"
    captcha_loc = "div[style*='visible;'] iframe[title*='recaptcha']"

    def submit_email(self):
        Waiter.wait_until_captcha_is_visible(By.CSS_SELECTOR, self.captcha_loc)
        self.get_submit_button().click()

    def get_input_login_field(self, login):
        return InputField(By.XPATH, self.input_login_field_loc_pattern % login, "Input field for sending link to email")

    def is_login_displayed(self, login):
        Waiter.wait_for_clickable(By.XPATH, self.input_login_field_loc_pattern % login)
        return self.get_input_login_field(login).is_displayed()

    def get_submit_button(self):
        return Button(By.XPATH, self.submit_button_loc, "Button to submit email")
