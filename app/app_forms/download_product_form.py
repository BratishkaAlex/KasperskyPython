from selenium.webdriver.common.by import By

from framework.elements.link import Link


class DownloadProductForm:
    send_by_email_link_loc = "//div[@class='w-downloadProductCard__sendLink']"

    def is_displayed(self):
        return self.get_send_by_email_link().is_displayed()

    def send_link_by_mail(self):
        self.get_send_by_email_link().click()

    def get_send_by_email_link(self):
        return Link(By.XPATH, self.send_by_email_link_loc, "Link to send link for download product")
