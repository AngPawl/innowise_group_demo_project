import allure
from allure_commons.types import Severity

from innowise_group_demo_project.components.header_menu import header_menu
from innowise_group_demo_project.pages.main_page import main_page


@allure.title('User opens a new page via header menu')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_selected_page_opens():
    main_page.open()

    header_menu.open_selected_page('Technologies', 'Python')

    header_menu.selected_page_should_be_opened('Python development company')
