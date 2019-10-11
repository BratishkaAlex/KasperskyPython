from app.app_forms.header import Header
from app.app_forms.navigation_menu import NavigationMenu


class MainPage:

    def __init__(self):
        self.__header = Header()
        self.__navigation_menu = NavigationMenu()

    @property
    def header(self):
        return self.__header

    @property
    def navigation_menu(self):
        return self.__navigation_menu
