from dotenv import load_dotenv
load_dotenv()
import os
from db.database import SessionLocal, engine
from fastapi import FastAPI, Depends, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from starlette.responses import RedirectResponse
from db import crud, models, schemas
import random
import string


models.Base.metadata.create_all(bind=engine)


def random_string(string_length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()




@app.post("/create", response_model=schemas.Link)
def create_link(link: schemas.LinkCreate, db=Depends(get_db)):
    short_url = random_string(6)
    existing_link = crud.get_link(db=db, short_url=short_url)
    while existing_link is not None:
        short_url = random_string(6)
        existing_link = crud.get_link(db=db, short_url=short_url)

    link_dict = link.dict()
    link_dict.update({"short_url": short_url})
    return crud.create_link(db=db, link=link_dict)


app.mount("/dist", StaticFiles(directory=os.environ["FRONTEND_SRC"], html=True), name="dist")
@app.get("/dist")
def add_trailing_slash():
    return RedirectResponse("/dist/")

@app.get("/")
def dist():
    return RedirectResponse("/dist/")

@app.get("/{short_url}")
def redirect(short_url: str, db=Depends(get_db)):
    link = crud.get_link(db=db, short_url=short_url)
    if link is None:
        return Response(status_code=404)
    return RedirectResponse(link.original_url)


