from fastapi import APIRouter


router = APIRouter()


@router.get('/', response_model=bool)
def get_sample():
    return True
