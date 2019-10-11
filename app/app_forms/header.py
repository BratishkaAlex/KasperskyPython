from selenium.webdriver.common.by import By

from framework.elements.link import Link


class Header:
    login_loc = "//span[contains(@class,'user-email')]"

    def is_user_authorized(self, login):
        return self.get_login_link().get_text() == login

    def get_login_link(self):
        return Link(By.XPATH, self.login_loc, "Link to check user")
