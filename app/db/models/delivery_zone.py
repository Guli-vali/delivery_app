"""
Delivery zone model with DB related logic
"""
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

from app.db.utils import Base


class DeliveryZone(Base):
    'DeliveryZone database model'
    __tablename__ = 'delivery_zone'

    id = Column(Integer, primary_key=True)
    area = Column(Geometry('POLYGON'))
    courier = relationship("Courier")
