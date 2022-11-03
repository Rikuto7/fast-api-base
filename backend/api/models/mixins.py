from datetime import datetime
from typing import Any

from sqlalchemy import DateTime, Column as SAColumn


class Column(SAColumn):
    def __init__(self, *args: Any, **kwargs: Any):
        kwargs.setdefault('nullable', False)
        super().__init__(*args, **kwargs)


class TimestampMixin(object):
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
