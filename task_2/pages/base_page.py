from playwright.sync_api import Page


class BasePage:
    def __init__(self, url: str, page: Page):
        self.url = url
        self.page = page

    def open(self):
        self.page.goto(self.url)
