import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


def pytest_addoption(parser):
    parser.addoption("--browser_url", default='', required=False)
    parser.addoption("--headless", default=False, required=False)


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_setup(request):
    browser_url = request.config.getoption("--browser_url")
    headless_mode = request.config.getoption("--headless")

    options = Options()

    options.add_argument("window-size=2800,1400")
    browser.config.base_url = "https://innowise-group.com/"

    if browser_url:
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "100",
            "selenoid:options": {"enableVNC": True, "enableVideo": True},
        }
        options.capabilities.update(selenoid_capabilities)

        login = os.getenv("LOGIN")
        password = os.getenv("PASSWORD")

        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@{browser_url}",
            options=options,
        )

        browser.config.driver = driver

    if headless_mode == 'True':
        options.add_argument("--headless")

    browser.config.driver_options = options

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
