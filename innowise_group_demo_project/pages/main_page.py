import allure
from selene import browser


class MainPage:
    @staticmethod
    @allure.step('Open Main Page')
    def open():
        browser.open('/')


main_page = MainPage()
