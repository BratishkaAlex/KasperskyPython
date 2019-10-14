from selenium.webdriver.common.by import By

from framework.elements.button import Button


class SelectProductMenu:
    id_attribute_name = "data-application-id"
    downloads_product_pattern = "//kl-carousel-item[@aria-hidden='false']//button[contains(@class, " \
                                "'jsDownloadApplications')][..//div[contains(text(), '%s')]]"

    def download_product(self, product):
        self.get_download_product_button(product).wait_and_click()

    def get_app_id(self, product):
        return int(self.get_download_product_button(product).get_attribute(self.id_attribute_name))

    def get_download_product_button(self, product):
        return Button(By.XPATH, self.downloads_product_pattern % product, "Download button for %s" % product)
