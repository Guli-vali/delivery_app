"""
Delivery zone ralated pydantic models
"""
from typing import List

from pydantic import BaseModel, Field


class GeoPoint(BaseModel):
    'Base model for geo points'
    long: str
    lat: str


class DeliveryZone(BaseModel):
    'Base model for all childs'
    id_: int = Field(0, alias="id")
    area: str


class DeliveryZoneInCreate(BaseModel):
    'DTO for creating delivery_zone objects'
    area: List[GeoPoint]


class DeliveryZoneInResponse(BaseModel):
    'DTO for response representation of delivery_zone'
    id_: int = Field(0, alias="id")
