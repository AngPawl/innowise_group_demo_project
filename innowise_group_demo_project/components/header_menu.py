import allure

from selene import browser, have
from selene.support.conditions.have import exact_text


class HeaderMenu:
    def __init__(self):
        self.menu_titles = browser.all('.new-menu .title-section a')
        self.page_names = browser.all('.co-technologies .content-section-in span a')
        self.selected_page_title = browser.element(
            '.elementor-section .container-header h1'
        )

    @allure.step('Open {target_page_name} page')
    def open_selected_page(self, section_name, target_page_name):
        self.menu_titles.element_by(exact_text(section_name)).hover()
        self.page_names.element_by(exact_text(target_page_name)).click()

    @allure.step('The page title should be {title}')
    def selected_page_should_be_opened(self, title):
        self.selected_page_title.should(have.exact_text(title))


header_menu = HeaderMenu()
