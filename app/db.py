import sqlite3


def create_schema():
    # define connection and cursor - c
    connection = sqlite3.connect('my_book.db')
    c = connection.cursor()

    c.executescript(""" DROP TABLE IF EXISTS books; DROP TABLE IF EXISTS comments """)

    # create books table
    command1 = """CREATE TABLE IF NOT EXISTS
    books(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT UNIQUE, author TEXT)"""
    c.execute(command1)

    # create comments table
    command2 = """CREATE TABLE IF NOT EXISTS
    comments(id INTEGER PRIMARY KEY AUTOINCREMENT, book_id INTEGER, comment TEXT, nickname TEXT)"""
    c.execute(command2)
