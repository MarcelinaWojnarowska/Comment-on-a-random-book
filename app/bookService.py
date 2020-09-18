import random
import sqlite3
import requests


class BookService:
    def insert_titles(self):
        google_books = requests.get('https://www.googleapis.com/books/v1/volumes?q=inauthor:%22stephen+king%22').json()
        connection = sqlite3.connect('my_book.db')
        c = connection.cursor()

        for item in google_books['items']:
            title = item['volumeInfo']['title']
            author = ", ".join(item['volumeInfo']['authors'])
            c.execute("REPLACE INTO books (title, author)"
                      "VALUES(?, ?)", (title, author))

        connection.commit()

    def get_random_book(self):
        connection = sqlite3.connect('my_book.db')
        c = connection.cursor()
        c.execute("SELECT * FROM books")
        results = c.fetchall()
        index = random.randrange(0, len(results))
        random_book = results[index]
        return random_book

    def get_titles(self):
        connection = sqlite3.connect('my_book.db')
        c = connection.cursor()
        c.execute("SELECT id, title FROM books")
        results = c.fetchall()
        return results

    def get_comments_for_book(self, id):
        connection = sqlite3.connect('my_book.db')
        c = connection.cursor()
        c.execute("SELECT comments.id, books.title, comments.comment, comments.nickname "
                  "FROM comments "
                  "JOIN books ON comments.book_id=books.id where books.id = ?", (id,))
        comment_data = c.fetchall()
        return comment_data
