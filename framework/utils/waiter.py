from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from framework.browser.browser import Browser
from resources import config


class Waiter:
    @staticmethod
    def implicit_wait(timeout):
        Browser.get_driver().implicitly_wait(timeout)

    @staticmethod
    def wait_for_clickable(by, element):
        WebDriverWait(Browser.get_driver(), config.timeout).until(
            expected_conditions.element_to_be_clickable((by, element)))

    @staticmethod
    def wait_until_captcha_is_visible(by, element):
        WebDriverWait(Browser.get_driver(), config.timeout_for_captcha).until(
            expected_conditions.invisibility_of_element_located((by, element)))
