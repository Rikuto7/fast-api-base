from sqlalchemy import Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship  # type: ignore

from backend.api.database import Base
from backend.api.models.mixins import Column, TimestampMixin


class Parent(Base, TimestampMixin):
    __tablename__ = 'parents'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))

    # one to one
    profile = relationship(  # type: ignore
        "Profile",
        backref="profile_parent",  # type: ignore
        uselist=False  # type: ignore
    )
    # one to many
    children = relationship(  # type: ignore
        "Child",
        backref="child_parent",  # type: ignore
        uselist=True  # type: ignore
    )
    # many to many
    jobs = relationship(  # type: ignore
        "Job",
        secondary="ParentJob",  # type: ignore
        uselist=True  # type: ignore
    )


# one to one
class Profile(Base, TimestampMixin):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(
        Integer, ForeignKey(Parent.id), unique=True
    )


# one to many
class Child(Base, TimestampMixin):
    __tablename__ = 'children'

    id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(
        Integer, ForeignKey(Parent.id)
    )


class Job(Base, TimestampMixin):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)

    parents = relationship(  # type: ignore
        "Parent",
        secondary="ParentJob",  # type: ignore
        uselist=True  # type: ignore
    )


# many to many
class ParentJob(Base, TimestampMixin):
    __tablename__ = 'parent_job'
    __table_args__ = (
        UniqueConstraint(
            'parent_id', 'job_id', name='unique_idx_parent_job'
        ),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(
        Integer, ForeignKey(Parent.id)
    )
    job_id = Column(
        Integer, ForeignKey(Job.id)
    )
