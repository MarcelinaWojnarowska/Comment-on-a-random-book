from flask import render_template, request
from app import app
from app.bookService import BookService
from app.commentService import CommentService

bookService = BookService()
commentService = CommentService()


@app.route('/')
def home():
    book = bookService.get_random_book()
    id, title, author = book
    return render_template('home.html', id=id, title=title)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/books')
def get_books():
    books = bookService.get_titles()
    return render_template('books.html', books=books)


@app.route('/addcomments', methods=['GET', 'POST'])
def add_comment():
    if request.method == 'GET':
        args = request.args
        id_book = args['id']
        title_book = args['title']
        return render_template('addcomment.html', id=id_book, title=title_book)
    else:
        comment_details = (
            request.form['id'],
            request.form['opinion'],
            request.form['nickname']
        )
        commentService.insert_comment(comment_details)
        return render_template('addsuccess.html')


@app.route('/comments')
def get_comments():
    comments = commentService.get_comment()
    return render_template('comments.html', comments=comments)


@app.route('/book/comments')
def book_comments():
    args = request.args
    id_book = args['id']
    comments = bookService.get_comments_for_book(id_book)
    return render_template('comments.html', comments=comments)
