import allure
from selene import browser


class SearchBox:
    def __init__(self):
        self.search_box = browser.element('.bot-serach-cli .form-sear-ico')
        self.input_field = browser.element('.new-block-sear .input-field')

    @allure.step('Send {query} as search query')
    def send_search_query(self, query):
        self.search_box.click()
        self.input_field.send_keys(query).press_enter()


search_box = SearchBox()
