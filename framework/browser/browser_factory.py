from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from resources import config


class BrowserFactory:
    @staticmethod
    def get_driver():
        if config.browser == "chrome":
            return webdriver.Chrome(ChromeDriverManager().install(),
                                    chrome_options=BrowserFactory.get_browser_options(config.browser))
        elif config.browser == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.set_preference("intl.accept_languages", str(config.language))
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_options=firefox_options)
        else:
            raise ValueError("Unknown browser")

    @staticmethod
    def get_browser_options(browser):
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            prefs = {"intl.accept_languages": str(config.language)}
            chrome_options.add_experimental_option("prefs", prefs)
            return chrome_options
        elif browser == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.set_preference("intl.accept_languages", str(config.language))
            return firefox_options
