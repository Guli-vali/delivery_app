"""
Endpoints ralated to delivery business purposes
"""
from random import randint

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.schemas.delivery_zone import GeoPoint
from app.models.schemas.courier import CourierInResponse
from app.models.schemas.delivery import DeliveryInResponse
from app.db.queries.delivery import POINT_WITHIN_ZONE, COURIERS_RELATED_TO_ZONE
from app.db.utils import get_db

router = APIRouter()


def courier_selection(couriers):
    """
    Helper for make decision which courier suitable for delivery,
    now implemented as random picking.
    """
    if not couriers:
        return []

    result = []
    courier_pointer = randint(0, len(couriers)-1)
    courier = couriers[courier_pointer]

    result.append(CourierInResponse(**courier._asdict()))
    return result


@router.post(
    "",
    name="delivery:create",
    status_code=status.HTTP_201_CREATED
)
async def delivery_event(
    delivery_point: GeoPoint,
    session: AsyncSession = Depends(get_db),
) -> DeliveryInResponse:
    'Calculates a suitable courier based on geolocation'
    zones_cursor = await session.execute(
                POINT_WITHIN_ZONE.format(
                    long=delivery_point.long,
                    lat=delivery_point.lat
                )
            )
    zones = zones_cursor.all()
    zone_ids = [i[0] for i in zones] if zones else []
    if not zone_ids:
        return HTTPException(
            status_code=404,
            detail="Couriers not found for this delivery point"
        )
    sql_prepared_zone_ids = ','.join([str(i) for i in zone_ids])
    couriers_fit_cursor = await session.execute(
                COURIERS_RELATED_TO_ZONE.format(sql_prepared_zone_ids)
            )
    couriers_fit = couriers_fit_cursor.all()

    selected_couries = courier_selection(couriers_fit)
    return DeliveryInResponse(data=selected_couries)
