import pytest
from selene import browser
from selenium import webdriver

from config import config
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    if config.browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        browser_version = '100'
    else:
        options = webdriver.FirefoxOptions()
        browser_version = '98'

    options.add_argument(f"window-size={config.window_width},{config.window_height}")

    if config.context == 'remote':
        selenoid_capabilities = {
            "browserName": config.browser_name,
            "browserVersion": browser_version,
            "selenoid:options": {"enableVNC": True, "enableVideo": True},
        }
        options.capabilities.update(selenoid_capabilities)

        login = config.login
        password = config.password
        browser_url = config.browser_url

        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@{browser_url}",
            options=options,
        )

        browser.config.driver = driver

    browser.config.driver_options = options
    browser.config.base_url = config.base_url

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)

    if config.browser_name == 'chrome':
        attach.add_logs(browser)

    attach.add_video(browser)

    browser.quit()
