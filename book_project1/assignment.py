from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title one", "author": "Author one", "category": "Science"},
    {"title": "Title two", "author": "Author two", "category": "Science"},
    {"title": "Title three", "author": "Author three", "category": "History"},
    {"title": "Title four", "author": "Author four", "category": "Maths"},
    {"title": "Title five", "author": "Author five", "category": "Maths"},
    {"title": "Title Six", "author": "Author two", "category": "Maths"},
    {"title": "Title Seven", "author": "Author two", "category": "Maths"},
]

''' Get all books from specific author using path or query parameter  '''

@app.get("/book/byauthor/{book_author}")
async def read_books_by_author_path(book_author: str):
    book_to_return = []
    for book in BOOKS:
        if book["author"].casefold() == book_author.casefold():
            book_to_return.append(book)

    return book_to_return