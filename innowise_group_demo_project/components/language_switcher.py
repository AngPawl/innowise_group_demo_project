import allure

from selene import browser, have
from selene.support.conditions.have import text

from innowise_group_demo_project.components.header_menu import header_menu


class LanguageSwitcher:
    def __init__(self):
        self.switcher = browser.element(
            '.new-block-lang .trp-ls-shortcode-current-language .trp-ls-shortcode-disabled-language'
        )
        self.language_list = browser.all('ul.translate-list-container > a > span')

    @allure.step('Switch language to {language}')
    def switch_language_to(self, language):
        self.switcher.hover()
        self.language_list.element_by(text(language)).click()

    @allure.step('The page should be successfully switched to {language}')
    def should_be_switched_to_language(self, language, translated_titles):
        self.switcher.should(have.exact_text(language))
        header_menu.menu_titles.should(have.exact_texts(*translated_titles))


language_switcher = LanguageSwitcher()
