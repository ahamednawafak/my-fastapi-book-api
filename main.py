from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str

books = [
    {"id": 1, "title": "The Hobbit"},
    {"id": 2, "title": "1984"}
]

@app.get("/")
def home():
    return {"message": "Welcome to my API!"}

@app.get("/books")
def get_books():
    return books

@app.post("/books")
def add_book(new_book: Book):
    books.append(new_book.model_dump())
    return {"message": "Book added successfully!", "book": new_book}

# DELETE Endpoint: Removes a book matching the given ID
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            removed_book = books.pop(index)
            return {"message": "Book deleted successfully!", "deleted_book": removed_book}
    
    raise HTTPException(status_code=404, detail="Book not found")