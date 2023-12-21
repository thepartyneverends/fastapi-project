from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

from database import engine

Base = declarative_base()


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)


Base.metadata.create_all(engine)
