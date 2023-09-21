import allure
from allure_commons.types import Severity

from innowise_group_demo_project.modal_forms.cookie_modal_form import cookie_modal_form
from innowise_group_demo_project.pages.main_page import main_page


@allure.title('The cookie modal form appears')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_cookie_modal_form_pops_up():
    main_page.open()

    cookie_modal_form.should_have_correct_title()
    cookie_modal_form.should_have_two_buttons()
    cookie_modal_form.should_have_correct_button_names()


@allure.title('The cookie modal form disappears when Reject All button is pressed')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_cookie_modal_form_disappears_on_reject_all():
    main_page.open()

    cookie_modal_form.should_disappear_on_reject_all()


@allure.title('The cookie modal form disappears when Accept All button is pressed')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_cookie_modal_form_disappears_on_accept_all():
    main_page.open()

    cookie_modal_form.should_disappear_on_accept_all()
