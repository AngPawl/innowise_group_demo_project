import allure
from allure_commons.types import Severity

from innowise_group_demo_project.components.language_switcher import language_switcher
from innowise_group_demo_project.pages.main_page import main_page


@allure.title('User switches the website language')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_language_switching_to_it():
    main_page.open()

    language_switcher.switch_language_to('Italiano')

    language_switcher.should_be_switched_to_language(
        'IT', ['Chi siamo', 'Servizi', 'Tecnologie', 'Industrie', 'Casi di studio']
    )
