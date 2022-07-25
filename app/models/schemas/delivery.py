"""
Delivery ralated pydantic models
"""
from typing import List

from pydantic import BaseModel

from app.models.schemas.courier import CourierInResponse


class DeliveryInResponse(BaseModel):
    'DTO for response representation of delivery objects'
    data: List[CourierInResponse]
