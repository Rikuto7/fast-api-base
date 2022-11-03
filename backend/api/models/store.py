from sqlalchemy import (
    Integer
)

from backend.api.database import Base
from backend.api.models.mixins import Column, TimestampMixin


class SampleModel(Base, TimestampMixin):
    __tablename__ = 'sample_model'

    id = Column(Integer, primary_key=True, autoincrement=True)
