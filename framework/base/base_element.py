from framework.browser.browser import Browser
from framework.utils.logger import Logger
from framework.utils.waiter import Waiter


class BaseElement:
    def __init__(self, by, loc, name):
        Logger.info(f"Creating instance of {name}")
        self.__by = by
        self.__loc = loc
        self.__name = name
        self.__webelement = Browser.get_driver().find_element(by, loc)

    def is_displayed(self):
        return self.__webelement.is_displayed()

    def click(self):
        self.__webelement.click()

    def wait_and_click(self):
        Waiter.wait_for_clickable(self.by, self.__loc)
        self.__webelement.click()

    def get_attribute(self, attribute):
        return self.__webelement.get_attribute(attribute)

    def get_text(self):
        return self.__webelement.text

    @property
    def webelement(self):
        return self.__webelement

    @property
    def by(self):
        return self.__by

    @property
    def loc(self):
        return self.__loc
