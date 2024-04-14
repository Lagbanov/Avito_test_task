from pydantic import BaseModel, Field


class DataFields(BaseModel):
    co2: int
    energy: int
    materials: int
    pine_years: int = Field(serialization_alias='pineYears')
    water: int


class Data(BaseModel):
    data: DataFields


class PersonalImpact(BaseModel):
    personal_impact: Data = Field(serialization_alias='personalImpact')


class Blocks(BaseModel):
    blocks: PersonalImpact
    is_authorized: bool = Field(default=False, serialization_alias='isAuthorized')


class EcoImpactInitResponse(BaseModel):
    result: Blocks
    status: str = 'ok'
