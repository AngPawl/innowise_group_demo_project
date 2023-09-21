import allure
from allure_commons.types import Severity

from innowise_group_demo_project.components.search_box import search_box
from innowise_group_demo_project.pages.main_page import main_page
from innowise_group_demo_project.pages.search_results import search_results_page


@allure.title('Search results appear for valid query')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_search_results_appear():
    main_page.open()

    search_box.send_search_query('qa automation')

    search_results_page.search_results_block_should_include_search_query(
        'qa automation'
    )
    search_results_page.search_filters_should_appear()
    search_results_page.articles_should_appear()


@allure.title('Search results don\'t appear for invalid query')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_search_results_doesnt_appear():
    main_page.open()

    search_box.send_search_query('abracadabra')

    search_results_page.should_return_no_results('abracadabra')
