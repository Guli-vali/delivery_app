"""
Courier ralated pydantic models
"""
from pydantic import BaseModel, Field


class CourierBase(BaseModel):
    'Base model for all childs'
    first_name: str
    last_name: str
    zone_id: int


class Courier(CourierBase):
    'Courier representation with id'
    id_: int = Field(0, alias="id")


class CourierInCreate(CourierBase):
    'DTO for creating courier objects'


class CourierInResponse(Courier):
    'DTO for response representation of courier'
