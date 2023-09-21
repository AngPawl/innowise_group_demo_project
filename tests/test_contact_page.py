import allure
from allure_commons.types import Severity

from innowise_group_demo_project.pages.contact_us import contact_us_page
from innowise_group_demo_project.pages.main_page import main_page


@allure.title('Contact Us page successfully opens via Let\'s Talk button')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_contact_us_page_opens():
    main_page.open()

    contact_us_page.open()

    contact_us_page.should_be_opened()
