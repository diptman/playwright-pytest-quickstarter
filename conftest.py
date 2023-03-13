import logging

from playwright.sync_api import Page, Playwright
import pytest
from playwright.sync_api import Playwright


def pytest_addoption(parser):
    parser.addoption('--browsers', action='store', default='chromium', help='Comma-separated list of browsers to test')


@pytest.fixture(scope="function", autouse=True)
def navigate_to_application(page: Page):
    logging.info("# Going to Sauce Demo Application")
    # Go to the starting url before each test.
    page.goto("https://www.saucedemo.com/")
    yield
    logging.info("Post function step")
