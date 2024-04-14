from playwright.sync_api import Page


class EcoImpactLocators:
    def __init__(self, page: Page):
        self.page = page

    @property
    def eco_contribution_locator(self):
        return self.page.locator('[class^="desktop-impact-items"]')

    @property
    def eco_contribution_water(self):
        return self.page.locator('//div[@class="desktop-impact-item-eeQO3"][.//*[text()="было сохранено"]]')

    @property
    def eco_contribution_co2(self):
        return self.page.locator('//div[@class="desktop-impact-item-eeQO3"][.//*[text()="не попало в атмосферу"]]')

    @property
    def eco_contribution_energy(self):
        return self.page.locator('//div[@class="desktop-impact-item-eeQO3"][.//*[text()="было сэкономлено"]]')