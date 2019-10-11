from selenium.webdriver.common.by import By

from framework.elements.button import Button


class SelectOsMenu:
    os_loc_pattern = "//div[@class='u-osTile__title' and text()='%s']"

    def select_os(self, os):
        self.get_button_for_os(os).wait_and_click()

    def get_button_for_os(self, os):
        return Button(By.XPATH, self.os_loc_pattern % os, "Button to navigate for %s downloads" % os)
