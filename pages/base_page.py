from typing import Literal
from typing import Pattern
import allure
from playwright.sync_api import Page, expect


class BasePage:
    WAIT_UNTIL: Literal["commit", "domcontentloaded", "load", "networkidle"] = "networkidle"

    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f'Opening the url "{url}"'):
            self.page.goto(url=url, wait_until=self.WAIT_UNTIL)

    def reload(self):
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            self.page.reload(wait_until=self.WAIT_UNTIL)

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking that current url matches pattern "{expected_url.pattern}"'):
            expect(self.page).to_have_url(expected_url)
