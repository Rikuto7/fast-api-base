import os
from typing import Any, Generator

from sqlalchemy.orm.scoping import ScopedSessionMixin
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base  # type: ignore

from sqlalchemy.engine.base import Engine
from sqlalchemy import create_engine  # type: ignore


DB_USER = os.environ.get('MYSQL_USER')
DB_PASSWORD = os.environ.get('MYSQL_PASSWORD')
DB_HOST = os.environ.get('MYSQL_HOST')
DB_PORT = os.environ.get('MYSQL_PORT')
DB_NAME = os.environ.get('MYSQL_DATABASE')

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8mb4' % (
    DB_USER,
    DB_PASSWORD,
    f'{DB_HOST}:{DB_PORT}',
    DB_NAME,
)

engine: Engine = create_engine(  # type: ignore
    DATABASE,
    encoding='utf-8',
    echo=True
)

SessionLocal: ScopedSessionMixin = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base: Any = declarative_base()
Base.query = SessionLocal.query_property()


def get_db() -> Generator[Session, None, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
