from sqlalchemy import Column, Integer, Text
from db import Base

class Book(Base):
    __tablename__ = "books"
    # Simple book entity stored in SQLite.
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(Text, nullable=False)
    author = Column(Text, nullable=False)
    year = Column(Integer, nullable=True)

