# Project 2: Setup
from fastapi import Body, FastAPI

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

BOOKS = [
    Book(1, 'Computer Science', 'codingwithroby', 'A very nice book!', 5),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A very great book!', 5),
    Book(3, 'Computer A', 'author 1', 'good book!', 5),
    Book(4, 'Computer B', 'author 2', 'good good book!', 2),
    Book(5, 'Computer C', 'author 3', 'awesomg book!', 3),
    Book(6, 'Computer D', 'author 4', 'hey hey book!', 1)
]

@app.get("/books")
async def read_all_books():
    return BOOKS
# --------------------------------
@app.post("/create_book")
async def create_book(book_request=Body()):
    BOOKS.append(book_request)