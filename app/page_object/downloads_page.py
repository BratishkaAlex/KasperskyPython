from selenium.webdriver.common.by import By

from app.app_forms.download_product_form import DownloadProductForm
from app.app_forms.select_os_menu import SelectOsMenu
from app.app_forms.select_product_menu import SelectProductMenu
from app.app_forms.send_by_email_form import SendByEmailForm
from framework.elements.label import Label


class DownloadsPage:
    downloads_label_loc = "//h2[@data-at-selector='downloadBlockTrialAppsTitle']"

    def __init__(self):
        self.__select_os_menu = SelectOsMenu()
        self.__select_product_menu = SelectProductMenu()
        self.__download_product_form = DownloadProductForm()
        self.__send_by_email_form = SendByEmailForm()

    def is_displayed(self):
        return self.get_download_page_label().is_displayed()

    @property
    def select_os_menu(self):
        return self.__select_os_menu

    @property
    def select_product_menu(self):
        return self.__select_product_menu

    @property
    def download_product_form(self):
        return self.__download_product_form

    @property
    def send_by_email_form(self):
        return self.__send_by_email_form

    def get_download_page_label(self):
        return Label(By.XPATH, self.downloads_label_loc, "Label for checking downloads page")
