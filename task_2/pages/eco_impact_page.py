from playwright.sync_api import Page, Route

from pages.base_page import BasePage
from pages.locators.eco_impact_locators import EcoImpactLocators
from schemas.eco_impact_init import Blocks, Data, DataFields, EcoImpactInitResponse, PersonalImpact


class EcoImpactPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(url='https://www.avito.ru/avito-care/eco-impact', page=page)
        self.screen = EcoImpactLocators(page)

    @staticmethod
    def __prepare_json_eco_impact(
            co2: int,
            energy: int,
            materials: int,
            pine_years: int,
            water: int,
    ):
        return EcoImpactInitResponse(
            result=Blocks(
                blocks=PersonalImpact(
                    personal_impact=Data(
                        data=DataFields(
                            co2=co2,
                            energy=energy,
                            materials=materials,
                            pine_years=pine_years,
                            water=water,
                        )
                    )
                ),
                is_authorized=False
            ),
            status='ok'
        ).model_dump(mode='json', by_alias=True)

    def handle(
            self,
            co2: int,
            energy: int,
            materials: int,
            pine_years: int,
            water: int,
    ):
        json_data = self.__prepare_json_eco_impact(
            co2=co2,
            energy=energy,
            materials=materials,
            pine_years=pine_years,
            water=water
        )

        def wrapper(route: Route):
            route.fulfill(json=json_data)

        return wrapper

    def route(
            self,
            co2: int,
            energy: int,
            materials: int,
            pine_years: int,
            water: int,
    ):
        self.page.route("*/**/web/1/charity/ecoImpact/init", self.handle(
            co2=co2,
            energy=energy,
            materials=materials,
            pine_years=pine_years,
            water=water
        )
                        )
