from pydantic import BaseModel, Field

class BookBase(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    year: int | None = Field(default=None, ge=0)

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1)
    author: str | None = Field(default=None, min_length=1)
    year: int | None = Field(default=None, ge=0)

class BookRead(BookBase):
    id: int
    class Config:
        from_attributes = True

class BookDelete(BaseModel):
    book_id: int
