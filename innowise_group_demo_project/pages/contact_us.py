import allure
from selene import browser, have


class ContactUsPage:
    @allure.step('Open Contact Us page')
    def open(self):
        browser.element('a.talk-button').click()

    @allure.step('Contact Us page should be opened')
    def should_be_opened(self):
        browser.element('.elementor-widget-container .elementor-heading-title').should(
            have.exact_text('Contact us')
        )


contact_us_page = ContactUsPage()
