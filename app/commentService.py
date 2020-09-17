import sqlite3


class CommentService:
    def insert_comment(self, comment_details):
        connection = sqlite3.connect('my_book.db')
        c = connection.cursor()
        c.execute("INSERT INTO comments (book_id, comment, nickname) VALUES(?,?,?)", comment_details)

        connection.commit()

    def get_comment(self):
        connection = sqlite3.connect('my_book.db')
        c = connection.cursor()
        c.execute("SELECT comments.id, books.title, comments.comment, comments.nickname "
                  "FROM comments "
                  "JOIN books ON comments.book_id=books.id")
        comment_data = c.fetchall()
        return comment_data