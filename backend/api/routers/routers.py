from fastapi import APIRouter

from backend.api.routers.sample_router import sample

router = APIRouter()

router.include_router(sample.router, prefix='/', tags=['demo'])
