import pytest
from playwright.sync_api import Page

from pages.eco_impact_page import EcoImpactPage


@pytest.mark.parametrize('co2, energy, materials, pine_years, water, test_case', (
        (0, 0, 0, 0, 0, 'TK-1'),
        (999, 999, 999, 999, 999, 'TK-2'),
        (1000, 1000, 1000, 1000, 1000, 'TK-3'),
        (1500, 1500, 1500, 1500, 1500, 'TK-4'),
        (1000000, 1000000, 1000000, 1000000, 1000000, 'TK-5'),
        (1000000000000, 1000000000000, 1000000000000, 1000000000000, 1000000000000, 'TK-6'),
        (1000000000000000, 1000000000000000, 1000000000000000, 1000000000000000, 1000000000000000, 'TK-7'),
        (-1, -1, -1, -1, -1, 'TK-8'),
))
def test_screenshot_users_eco_contribution_counter(
        page: Page,
        co2: int,
        energy: int,
        materials: int,
        pine_years: int,
        water: int,
        test_case: str,
):
    test = EcoImpactPage(page)
    test.route(
        co2=co2,
        energy=energy,
        materials=materials,
        pine_years=pine_years,
        water=water,
    )
    test.open()
    test.screen.eco_contribution_locator.screenshot(path=f"output/{test_case}-full_counter.png")
    test.screen.eco_contribution_water.screenshot(path=f"output/{test_case}-water.png")
    test.screen.eco_contribution_co2.screenshot(path=f"output/{test_case}-co2.png")
    test.screen.eco_contribution_energy.screenshot(path=f"output/{test_case}-energy.png")
