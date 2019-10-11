from selenium.webdriver.common.by import By

from framework.elements.link import Link


class NavigationMenu:
    menu_link_pattern = ".is-showing-on-top .js-%s-nav-link"

    def navigateTo(self, menu_item):
        self.get_navigation_menu_link(menu_item).click()

    def get_navigation_menu_link(self, menu_item):
        return Link(By.CSS_SELECTOR, self.menu_link_pattern % menu_item, "Link to %s" % menu_item)
