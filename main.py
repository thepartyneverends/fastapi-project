from typing import Optional

from fastapi import FastAPI, Depends, Request
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

import crud
import models
import schemas
from database import SessionLocal

app = FastAPI()

# app.mount('/static', StaticFiles(directory='static'), name='static')


templates = Jinja2Templates(directory='templates')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/items/{item_id}/', response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@app.get('/items/{item_id}', response_model=list[schemas.Item])
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item_by_id(db, item_id=item_id)
    return item


@app.get('/items/', response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.get('/', response_class=HTMLResponse)
async def read_all_items(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return templates.TemplateResponse('index.html', {'request': request, 'items': items})


@app.get('/search/')
async def search(request: Request, db: Session = Depends(get_db), query: Optional[str] = None):
    result = crud.search_item(query=query, db=db)
    return templates.TemplateResponse('index.html', {'request': request, 'items': result})
