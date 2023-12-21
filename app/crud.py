from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import models
import schemas


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_item_by_id(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id)


def search_item(query: str, db: Session):
    result = db.query(models.Item).filter(models.Item.title.contains(query))
    return result


def delete_item(db: Session, item_id: int):
    item = db.get(models.Item, item_id)
    if not item:
        return f'Item {item_id} was not found.'
    db.delete(item)
    db.commit()
    return f'Item {item_id} successfully deleted.'


def update_item(db: Session, item_id: int, item: schemas.Item):
    update_item_encoded = jsonable_encoder(item)
    db_item = db.query(models.Item).filter(models.Item.id == item_id)
    db_item = update_item_encoded
    return db_item
