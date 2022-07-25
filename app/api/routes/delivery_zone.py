"""
Endpoints ralated to delivery zone business purposes
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.schemas.delivery_zone import \
    DeliveryZoneInCreate, DeliveryZoneInResponse
from app.db.queries.delivery_zone import INSERT_DELIVERY_ZONE_POLYGON
from app.db.utils import get_db

router = APIRouter()


@router.post(
    "",
    name="delivery_zone:create",
    status_code=status.HTTP_201_CREATED
)
async def create_delivery_zone(
    area: DeliveryZoneInCreate,
    session: AsyncSession = Depends(get_db),
) -> DeliveryZoneInResponse:
    """
    Creates delivery zone(Polygon) based on the \
     set of points with longitude and latitude
    """
    points = ['{long} {lat}'.format(long=i.long, lat=i.lat) for i in area.area]
    res = await session.execute(
                INSERT_DELIVERY_ZONE_POLYGON.format(','.join(points))
            )
    await session.commit()
    return DeliveryZoneInResponse(**{'id': res.fetchone()[0]})
