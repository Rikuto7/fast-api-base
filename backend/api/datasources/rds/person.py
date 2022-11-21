from backend.api import models
from backend.api.datasources.rds.base import CRUDBase


class CRUDStore(
    CRUDBase[models.Person, None, None]  # type: ignore
):
    pass


person_crud = CRUDStore(models.Person)
