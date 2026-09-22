from fastapi import FastAPI, HTTPException, Security, status
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

app = FastAPI()

# 1. Set your secret password here
API_PASSWORD = "MySecretPassword123"

# 2. Define the header name the user must send
api_key_header = APIKeyHeader(name="X-API-Key")

# Function to verify the password
def verify_password(api_key: str = Security(api_key_header)):
    if api_key != API_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing Password / API Key"
        )
    return api_key

class Book(BaseModel):
    id: int
    title: str

books = [
    {"id": 1, "title": "The Hobbit"},
    {"id": 2, "title": "1984"}
]

# Unprotected route (Anyone can see the home page)
@app.get("/")
def home():
    return {"message": "Welcome to my API!"}

# Protected route: Requires valid password
@app.get("/books", dependencies=[Security(verify_password)])
def get_books():
    return books

# Protected route: Requires valid password
@app.post("/books", dependencies=[Security(verify_password)])
def add_book(new_book: Book):
    books.append(new_book.model_dump())
    return {"message": "Book added successfully!", "book": new_book}

# Protected route: Requires valid password
@app.delete("/books/{book_id}", dependencies=[Security(verify_password)])
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            removed_book = books.pop(index)
            return {"message": "Book deleted successfully!", "deleted_book": removed_book}
    
    raise HTTPException(status_code=404, detail="Book not found")