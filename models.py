from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base

from database import engine

Base = declarative_base()


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    title = Column(String)


Base.metadata.create_all(engine)
