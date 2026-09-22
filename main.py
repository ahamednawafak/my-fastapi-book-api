from fastapi import FastAPI, HTTPException, Security, Depends, status
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# --- 1. DATABASE SETUP ---
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class DBBook(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

Base.metadata.create_all(bind=engine)


# --- 2. SECURITY SETUP ---
API_PASSWORD = "MySecretPassword123"
api_key_header = APIKeyHeader(name="X-API-Key")

def verify_password(api_key: str = Security(api_key_header)):
    if api_key != API_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing Password / API Key"
        )
    return api_key


# --- 3. FASTAPI APP & SCHEMAS ---
app = FastAPI()

class BookSchema(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True

# Schema specifically for updating a book's title
class BookUpdateSchema(BaseModel):
    title: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- 4. ENDPOINTS ---

@app.get("/")
def home():
    return {"message": "Welcome to my API connected to SQLite!"}

# GET /books
@app.get("/books", dependencies=[Security(verify_password)])
def get_books(db: Session = Depends(get_db)):
    books = db.query(DBBook).all()
    return books

# POST /books
@app.post("/books", dependencies=[Security(verify_password)])
def add_book(new_book: BookSchema, db: Session = Depends(get_db)):
    existing_book = db.query(DBBook).filter(DBBook.id == new_book.id).first()
    if existing_book:
        raise HTTPException(status_code=400, detail="Book with this ID already exists.")
    
    db_book = DBBook(id=new_book.id, title=new_book.title)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return {"message": "Book saved permanently to database!", "book": db_book}

# PUT /books/{book_id}: Update an existing book's details
@app.put("/books/{book_id}", dependencies=[Security(verify_password)])
def update_book(book_id: int, updated_book: BookUpdateSchema, db: Session = Depends(get_db)):
    db_book = db.query(DBBook).filter(DBBook.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Update title field
    db_book.title = updated_book.title
    db.commit()
    db.refresh(db_book)
    return {"message": "Book updated successfully!", "updated_book": db_book}

# DELETE /books/{book_id}
@app.delete("/books/{book_id}", dependencies=[Security(verify_password)])
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(DBBook).filter(DBBook.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(db_book)
    db.commit()
    return {"message": "Book permanently deleted from database!"}