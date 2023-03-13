import re
from playwright.sync_api import Page, expect


def test_login_to_sauce_demo_application(page: Page):
    expect(page).to_have_title(re.compile("Swag Labs"))
