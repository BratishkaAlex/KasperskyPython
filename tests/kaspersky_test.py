import pytest

from app.app_utils.links_checker import LinksChecker
from app.enums.navigation_menu import NavigationMenuItems
from app.page_object.downloads_page import DownloadsPage
from app.page_object.main_page import MainPage
from app.page_object.unauthorized_page import UnauthorizedPage
from framework.browser.browser import Browser
from framework.models.mail import Mail
from framework.utils.logger import Logger
from framework.utils.mail_utils import MailUtils
from framework.utils.waiter import Waiter
from resources import config


def idfn(val):
    return "params: {0}".format(str(val))


class TestKaspersky:
    counter = 1
    mail = Mail

    @pytest.fixture(scope="function", params=[
        ("Windows", "Password Manager"),
        ("Mac", "Internet Security"),
        ("Android", "Safe Kids")],
                    ids=idfn)
    def param_test(self, request):
        return request.param

    def setup_method(self):
        self.counter = 1
        Waiter.implicit_wait(config.timeout)
        Browser.maximize()
        self.mail = Mail(config.login, config.password)
        MailUtils.delete_all_emails(self.mail)

    def teardown_method(self):
        Browser.close_browser()

    def test_kasp(self, param_test):
        os, product = param_test
        Logger.info("Enter https://my.kaspersky.com")
        Browser.enter_url(config.url)

        Logger.step("Authorize on my.kaspersky.com", self.counter)
        self.counter += 1
        unauthorized_page = UnauthorizedPage()
        unauthorized_page.sign_in()
        unauthorized_page.sign_in_menu.log_in(config.login, config.password)

        main_page = MainPage()
        Logger.info("Checking that user authorized successfully")
        assert main_page.header.is_user_authorized(config.login), "User didn't authorize"

        Logger.step("Click on downloads", self.counter)
        self.counter += 1
        main_page.navigation_menu.navigateTo(NavigationMenuItems.downloads.name)

        downloads_page = DownloadsPage()
        Logger.info("Checking opening the download page")
        assert downloads_page.is_displayed(), "This is not the downloads page"
        downloads_page.select_os_menu.select_os(os)

        Logger.step("Click on download product for expected os", self.counter)
        self.counter += 1
        app_id = downloads_page.select_product_menu.get_app_id(product)
        downloads_page.select_product_menu.download_product(product)

        Logger.info("Checking opening the dialogue window for downloading")
        assert downloads_page.download_product_form.is_displayed(), "Dialogue window is not opened"

        Logger.step("Click on send link by email", self.counter)
        self.counter += 1
        downloads_page.download_product_form.send_link_by_mail()
        Logger.info("Checking opening the dialogue window for sending link by email")
        assert downloads_page.send_by_email_form.is_login_displayed(
            config.login), "Login is not entered automatically in input field"

        Logger.step("Click on submit email", self.counter)
        downloads_page.send_by_email_form.submit_email()
        Waiter.wait_while_email_received(self.mail)
        Logger.info("Checking that received mail contains link to download expected product")
        assert LinksChecker.contains_link_for_product_and_os(
            str(MailUtils.get_first_message(self.mail)), os, app_id)
