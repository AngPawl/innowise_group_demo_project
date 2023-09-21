import allure
from selene import browser, have


class SearchResultsPage:
    def __init__(self):
        self.search_results_block = browser.element('.search-block .search-result')
        self.search_filters = browser.all(
            '.category-filter-buttons > .category-filter-button'
        )
        self.articles = browser.all('article.article-search')

    @allure.step('The search results block should include {query}')
    def search_results_block_should_include_search_query(self, query):
        self.search_results_block.should(have.text(query))

    @allure.step('The search results filter should appear')
    def search_filters_should_appear(self):
        self.search_filters.should(have.size_greater_than(0))

    @allure.step('The search results articles should appear on the page')
    def articles_should_appear(self):
        self.articles.should(have.size_greater_than(0))

    @allure.step('No search results should appear for {query}')
    def should_return_no_results(self, query):
        self.search_results_block.should(have.text(f'no results for "{query}"'))
        self.search_filters.should(have.size(0))


search_results_page = SearchResultsPage()
