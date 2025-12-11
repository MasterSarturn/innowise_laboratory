from sqlalchemy.orm import Session
import models, schemas

def read_books(db: Session, skip=0, limit=100):
    """Return paginated list of books."""
    return db.query(models.Book).offset(skip).limit(limit).all()

def create_book(db: Session, data: schemas.BookCreate):
    """Create a book with normalized author field."""
    payload = data.dict()
    if payload.get("author"):
        payload["author"] = payload["author"].capitalize()
    book = models.Book(**payload)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    """Delete a book by id; return True if deleted."""
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        return False
    db.delete(book)
    db.commit()
    return True

def update_book(db: Session, book_id: int, data: schemas.BookUpdate):
    """Partially update a book; return updated entity or None."""
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        if field == "author" and value:
            value = value.capitalize()
        setattr(book, field, value)
    db.commit()
    db.refresh(book)
    return book

def search_books(db: Session, title: str | None = None, author: str | None = None, year: int | None = None):
    """Search by optional title/author and exact year."""
    query = db.query(models.Book)
    if title:
        query = query.filter(models.Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(models.Book.author.ilike(f"%{author}%"))
    if year is not None:
        query = query.filter(models.Book.year == year)
    return query.all()
