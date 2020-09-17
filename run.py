from app import app, db
from app.bookService import BookService

db.create_schema()
books = BookService()
books.insert_titles()

if __name__ == "__main__":
    app.run()

