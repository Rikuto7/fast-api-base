from fastapi import APIRouter

from backend.api.routers.endpoints.businesses import person

router = APIRouter()

router.include_router(person.router, prefix='', tags=['demo'])
