from flask import request, jsonify, make_response
from flask import current_app as app
from .models import *

@app.errorhandler(404) 
def not_found(e): 
    return '404'

@app.route('/api/')
def index():
    return 'Hello World!'

@app.route('/api/books', methods = ['GET'])
def get_books():
    get_books = Book.query.all()
    book_schema = BookSchema(many=True)
    books = book_schema.dump(get_books)
    return make_response(jsonify({"books": books}))

@app.route('/api/most_downloaded_books', methods = ['GET'])
def get_most_downloaded_books():
    get_books = Book.query.order_by(Book.download_ebook_count.desc()).limit(10)
    book_schema = BookSchema(many=True)
    books = book_schema.dump(get_books)
    return make_response(jsonify({"books": books}))

@app.route('/api/search', methods = ['GET'])
def search_books():
    search_string = request.args.get('book').strip()
    if not search_string:
        return make_response(jsonify({"books": []}))

    search = "%{}%".format(search_string)
    get_books = Book.query.filter(Book.title.like(search) | Book.author.like(search)).all()
    book_schema = BookSchema(many=True)
    books = book_schema.dump(get_books)
    return make_response(jsonify({"books": books}))

@app.route('/api/books/<id>', methods = ['GET'])
def get_book_by_id(id):
    get_book = Book.query.get(id)
    book_schema = BookSchema()
    book = book_schema.dump(get_book)

    get_series = Serie.query.filter_by(book_id=id)
    serie_schema = SerieSchema(many=True)
    series = serie_schema.dump(get_series)
    if series:
        return make_response(jsonify({"book": book, "series": series}))
    return make_response(jsonify({"book": book}))

@app.route('/api/books/<id>/read', methods = ['GET'])
def get_chapters_by_book_id(id):
    get_chapters = Chapter.query.filter_by(book_id=id).offset(0).limit(3)
    chapter_schema = ChapterSchema(many=True)
    chapters = chapter_schema.dump(get_chapters)
    return make_response(jsonify({"chapters": chapters}))

@app.route('/api/books/<book_id>/chapters/<chapter_id>', methods = ['GET'])
def get_chapter_by_id(book_id, chapter_id):
    get_chapter = Chapter.query.filter_by(book_id=book_id, chapter_id = chapter_id).first()
    print(get_chapter)
    chapter_schema = ChapterSchema()
    chapter = chapter_schema.dump(get_chapter)
    return make_response(jsonify({"chapter": chapter}))