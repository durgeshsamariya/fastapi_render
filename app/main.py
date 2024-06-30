from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Dict, List, Optional

app = FastAPI()

# In-memory database (dictionary) to store book details
books_db: Dict[int, Dict[str, str]] = {}

class Book(BaseModel):
    title: str
    author: str
    year: int

# Endpoint to add a new book
@app.post("/books/")
def create_book(book: Book):
    book_id = len(books_db) + 1
    books_db[book_id] = {
        "title": book.title,
        "author": book.author,
        "year": book.year
    }
    return {"message": "Book added successfully", "book_id": book_id}

# Endpoint to retrieve a book by ID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[book_id]

# Endpoint to retrieve all books
@app.get("/books/")
def get_all_books():
    return list(books_db.values())

# Endpoint to update a book by ID
@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    books_db[book_id] = {
        "title": book.title,
        "author": book.author,
        "year": book.year
    }
    return {"message": "Book updated successfully", "book_id": book_id}

# Endpoint to delete a book by ID
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    del books_db[book_id]
    return {"message": "Book deleted successfully", "book_id": book_id}
