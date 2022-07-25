"""
Courier model with DB related logic
"""
from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.utils import Base


class Courier(Base):
    'Courier database model'
    __tablename__ = 'couriers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    zone_id = Column(Integer, ForeignKey("delivery_zone.id"))
