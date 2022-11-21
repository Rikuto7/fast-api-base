from sqlalchemy import Integer, String, ForeignKey, UniqueConstraint, Boolean
from sqlalchemy.orm import relationship  # type: ignore

from backend.api.database import Base
from backend.api.models.mixins import Column, TimestampMixin


class Person(Base, TimestampMixin):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))

    # one to one
    profile = relationship(  # type: ignore
        "Profile",
        backref="profile_person",  # type: ignore
        uselist=False  # type: ignore
    )
    # one to many
    articles = relationship(  # type: ignore
        "Article",
        backref="article_person",  # type: ignore
        primaryjoin="and_(Person.id==Article.person_id, Article.is_delete==False)",  # type: ignore
        uselist=True  # type: ignore
    )
    # many to many different table
    jobs = relationship(  # type: ignore
        "Job",
        secondary="PersonJob",  # type: ignore
        uselist=True  # type: ignore
    )
    # # many to many same table
    # follows = relationship(   # type: ignore
    #     'Person',
    #     secondary="FriendlyShip",  # type: ignore
    #     uselist=True  # type: ignore
    # )
    # followers = relationship(   # type: ignore
    #     'Person',
    #     secondary="FriendlyShip",  # type: ignore
    #     uselist=True  # type: ignore
    # )


# one to one
class Profile(Base, TimestampMixin):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    person_id = Column(
        Integer, ForeignKey(Person.id), unique=True
    )


# one to many
class Article(Base, TimestampMixin):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    person_id = Column(
        Integer, ForeignKey(Person.id)
    )
    is_delete = Column(Boolean, default=False)


class Job(Base, TimestampMixin):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)

    persons = relationship(  # type: ignore
        "Person",
        secondary="PersonJob",  # type: ignore
        uselist=True  # type: ignore
    )


# many to many
class PersonJob(Base, TimestampMixin):
    __tablename__ = 'person_job'
    __table_args__ = (
        UniqueConstraint(
            'person_id', 'job_id', name='unique_idx_person_job'
        ),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    person_id = Column(
        Integer, ForeignKey(Person.id)
    )
    job_id = Column(
        Integer, ForeignKey(Job.id)
    )


class FriendlyShip(Base, TimestampMixin):
    __tablename__ = 'friendly_ships'

    id = Column(Integer, primary_key=True, autoincrement=True)
    follow_id = Column(
        Integer, ForeignKey(Person.id)
    )
    follower_id = Column(
        Integer, ForeignKey(Person.id)
    )

    # many to many same table
    follows = relationship(   # type: ignore
        'Person',
        backref="follows",  # type: ignore
        primaryjoin=(Person.id == follow_id),  # type: ignore
        uselist=True  # type: ignore
    )
    followers = relationship(   # type: ignore
        'Person',
        backref="followers",  # type: ignore
        primaryjoin=(Person.id == follower_id),  # type: ignore
        uselist=True  # type: ignore
    )
