import allure
from selene import browser, have, be


class CookieModalForm:
    def __init__(self):
        self.title = browser.element(
            '.elementor-location-popup .elementor-heading-title'
        )
        self.buttons = browser.all('.elementor-location-popup a.elementor-button')
        self.button_texts = browser.all(
            '.elementor-location-popup span.elementor-button-text'
        )
        self.modal_form = browser.element('dialog-message dialog-lightbox-message')

    @allure.step('The cookie modal form should have the correct title')
    def should_have_correct_title(self):
        self.title.should(have.exact_text('This website uses cookies'))

    @allure.step('The cookie modal form should have 2 buttons')
    def should_have_two_buttons(self):
        self.buttons.should(have.size(2))

    @allure.step('The cookie modal form buttons should have correct names')
    def should_have_correct_button_names(self):
        self.button_texts.should(have.exact_texts('Reject all', 'Accept all'))

    @allure.step(
        'The cookie modal form should disappear after button Reject All is pressed'
    )
    def should_disappear_on_reject_all(self):
        self.buttons.first.click()
        self.modal_form.should(be.absent)

    @allure.step(
        'The cookie modal form should disappear after button Accept All is pressed'
    )
    def should_disappear_on_accept_all(self):
        self.buttons.first.click()
        self.modal_form.should(be.absent)


cookie_modal_form = CookieModalForm()
