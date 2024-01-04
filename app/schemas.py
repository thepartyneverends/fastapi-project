from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    title: str
    description: str

    class Config:
        from_attributes = True


class ItemUpdate(ItemBase):
    title: Optional[str] = None
    description: Optional[str] = None
