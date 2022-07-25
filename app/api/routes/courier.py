"""
Endpoints ralated to courier business purposes
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.schemas.courier import CourierInCreate, CourierInResponse
from app.db.queries.courier import INSERT_COURIER
from app.db.utils import get_db

router = APIRouter()


@router.post(
    "",
    name="courier:create",
    status_code=status.HTTP_201_CREATED
)
async def create_courier(
    courier_data: CourierInCreate,
    session: AsyncSession = Depends(get_db),
) -> CourierInResponse:
    'Simply creates a courier with assigned zone of delivery'
    res = await session.execute(
                INSERT_COURIER.format(
                    first_name=courier_data.first_name,
                    last_name=courier_data.last_name,
                    zone_id=str(courier_data.zone_id)
                )
            )
    await session.commit()

    created_courier = res.fetchone()
    return CourierInResponse(**created_courier._asdict())
