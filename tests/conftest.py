import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    options = Options()

    options.add_argument("window-size=2800,1400")

    environment = os.getenv("ENVIRONMENT")

    if environment == 'selenoid':
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "100",
            "selenoid:options": {"enableVNC": True, "enableVideo": True},
        }
        options.capabilities.update(selenoid_capabilities)

        login = os.getenv("LOGIN")
        password = os.getenv("PASSWORD")
        browser_url = os.getenv("BROWSER_URL")

        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@{browser_url}",
            options=options,
        )

        browser.config.driver = driver

    browser.config.driver_options = options
    browser.config.base_url = "https://innowise-group.com/"

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
