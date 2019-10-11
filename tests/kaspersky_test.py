from app.enums.navigation_menu import NavigationMenuItems
from app.page_object.downloads_page import DownloadsPage
from app.page_object.main_page import MainPage
from app.page_object.unauthorized_page import UnauthorizedPage
from framework.browser.browser import Browser
from framework.utils.waiter import Waiter
from resources import config


class TestKaspersky:

    def setup_class(cls):
        Waiter.implicit_wait(config.timeout)
        Browser.maximize()

    def teardown_class(cls):
        Browser.close_browser()

    def test_kasp(self):
        Browser.enter_url(config.url)
        unauthorized_page = UnauthorizedPage()
        unauthorized_page.sign_in()
        unauthorized_page.sign_in_menu.log_in("test09162019@gmail.com", "Qwerty123!")
        main_page = MainPage()
        assert main_page.header.is_user_authorized("test09162019@gmail.com"), "User didn't authorize"
        main_page.navigation_menu.navigateTo(NavigationMenuItems.downloads.name)
        downloads_page = DownloadsPage()
        assert downloads_page.is_displayed(), "This is not the downloads page"
        downloads_page.select_os_menu.select_os("Mac")
        app_id = downloads_page.select_product_menu.get_app_id("Password Manager")
        downloads_page.select_product_menu.download_product("Password Manager")
        assert downloads_page.download_product_form.is_displayed(), "Dialogue window is not opened"
        downloads_page.download_product_form.send_link_by_mail()
        assert downloads_page.send_by_email_form.is_login_displayed(
            "test09162019@gmail.com"), "Login is not entered automatically in input field"
        downloads_page.send_by_email_form.submit_email()
