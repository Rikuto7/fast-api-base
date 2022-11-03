from backend.api import models
from backend.api.datasources.rds.base import CRUDBase


class CRUDStore(
    CRUDBase[models.SampleModel, None, None]  # type: ignore
):
    pass


sample_crud = CRUDStore(models.SampleModel)
