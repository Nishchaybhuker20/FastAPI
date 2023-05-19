from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class Film(Base):
    __tablename__= "films"

    id = Column(Integer, primary_key=True, index=True)
    NameError = Column(String, unique=True, index=True)
    director = Column(String)

