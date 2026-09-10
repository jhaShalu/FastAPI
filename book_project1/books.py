from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title one", "author": "Author one", "category": "Science"},
    {"title": "Title two", "author": "Author two", "category": "Science"},
    {"title": "Title three", "author": "Author three", "category": "History"},
    {"title": "Title four", "author": "Author four", "category": "Maths"},
    {"title": "Title five", "author": "Author five", "category": "Maths"},
    {"title": "Title Six", "author": "Author two", "category": "Maths"},
]


@app.get("/api-endpoint")
async def first_api():
    return {"message": "Hello Eric!"}


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            return book

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book["category"].casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

@app.get("/books/{author}/")
async def read_author_category_by_query(author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book["author"].casefold() == author.casefold() and book["category"].casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/book/create_book/")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)


@app.put("/book/update_book/")
async def update_book(updated_book = Body()):
    for i  in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book


@app.delete("/book/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break



