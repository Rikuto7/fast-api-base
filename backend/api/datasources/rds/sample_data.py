from backend.api import models
from backend.api.datasources.rds.base import CRUDBase


class CRUDStore(
    CRUDBase[models.Parent, None, None]  # type: ignore
):
    pass


parent_crud = CRUDStore(models.Parent)
