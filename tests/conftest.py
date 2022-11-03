import pytest, os
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_preconfig():
    browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.hold_browser_open = (
            os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
    )
    browser.config.timeout = float(os.getenv('selene.timeout', '5'))
    yield