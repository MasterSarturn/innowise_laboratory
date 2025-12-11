from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from db import Base, engine, get_db
import uvicorn

# Ensure tables exist at startup.
models
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/books", tags=["view books"], response_model=list[schemas.BookRead], summary="List all books")
def read_books(db: Session = Depends(get_db)):
    return crud.read_books(db)

@app.post("/books", response_model=schemas.BookRead, status_code=201, summary="Create a new book")
def create_book(data: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, data)

@app.delete("/books/{book_id}", status_code=204, summary="Delete a book")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    if not crud.delete_book(db, book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return None 

@app.put("/books/{book_id}", response_model=schemas.BookRead, status_code=200, summary="Update a book")
def update_book(book_id: int, data: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = crud.update_book(db, book_id, data)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.get("/books/search", tags = ["view books"], response_model=list[schemas.BookRead], summary="Search books")
def search_books(
    title: str | None = None,
    author: str | None = None,
    year: int | None = None,
    db: Session = Depends(get_db),
):
    if title is None and author is None and year is None:
        raise HTTPException(status_code=400, detail="Provide at least one search parameter")
    return crud.search_books(db, title=title, author=author, year=year)


if __name__=="__main__":
    uvicorn.run("main:app", reload =True)