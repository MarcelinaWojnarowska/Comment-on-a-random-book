import sqlite3


def create_schema():
    # define connection and cursor - c
    connection = sqlite3.connect('my_book.db')
    c = connection.cursor()

    c.executescript(""" DROP TABLE IF EXISTS books; DROP TABLE IF EXISTS comments; 
    CREATE TABLE IF NOT EXISTS
    books(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT UNIQUE, author TEXT);
    CREATE TABLE IF NOT EXISTS
    comments(id INTEGER PRIMARY KEY AUTOINCREMENT, book_id INTEGER, comment TEXT, nickname TEXT)""")


