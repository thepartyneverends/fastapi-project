from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str


class ItemCreate(ItemBase):
    title: str


class Item(ItemBase):
    id: int
    title: str

    class Config:
        from_attributes = True
