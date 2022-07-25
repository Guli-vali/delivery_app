"""
Setting up routes for all endpoint modules
"""
from fastapi import APIRouter

from app.api.routes import delivery_zone, courier, delivery

router = APIRouter()
router.include_router(
    delivery_zone.router, tags=["delivery-zone"], prefix="/delivery-zone")
router.include_router(
    courier.router, tags=["courier"], prefix="/courier")
router.include_router(
    delivery.router, tags=["delivery"], prefix="/delivery")
