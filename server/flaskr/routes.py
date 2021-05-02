from flask import request, jsonify, make_response
from flask import current_app as app
from flask_cors import CORS
from flask_caching import Cache
from .models import *
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
) 
cache = Cache(config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 300})
cache.init_app(app)
CORS(app)

@app.errorhandler(404) 
def not_found(e): 
    return '404'

@app.route('/api/')
@limiter.limit("1 per day")
def index():
    return 'Dushu API'

@app.route('/api/books', methods = ['GET'])
@cache.memoize(3000)
def get_books():
    get_books = Book.query.all()
    book_schema = BookSchema(many=True)
    books = book_schema.dump(get_books)
    return make_response(jsonify({"books": books}))

@app.route('/api/books/<id>', methods = ['GET'])
@cache.cached()
def get_book_by_id(id):

    get_series = Serie.query.filter_by(book_id=id)
    serie_schema = SerieSchema(many=True)
    series = serie_schema.dump(get_series)
    if series:
        return make_response(jsonify({"series": series}))

    get_chapters = Chapter.query.filter_by(book_id=id)
    chapter_schema = ChapterSchema(many=True)
    chapters = chapter_schema.dump(get_chapters)
    if chapters:
        return make_response(jsonify({ "chapters": chapters}))
    return make_response(jsonify({"book": 'Not Found'}))


@app.route('/api/books/<id>/ebook-download', methods = ['GET'])
@limiter.limit("1 per minute")
def download_ebook(id):
    count = Book.download_ebook(id)
    cache.delete_memoized(get_books)
    return make_response(jsonify({"id": id, "download_ebook_count": count}))

@app.route('/api/books/<id>/pdf-download', methods = ['GET'])
@limiter.limit("1 per minute")
def download_pdf(id):
    count = Book.download_pdf(id)
    cache.delete_memoized(get_books)
    return make_response(jsonify({"id": id, "download_pdf_count": count}))

# search record
@app.route('/api/q', methods = ['GET'])
@limiter.limit("10 per minute")
def search():
    search_string = request.args.get('book').strip()
    search_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    if not search_string or not search_ip:
        return make_response(jsonify({"success": False, 'msg': 'no search string'}))
    newSearch = Search(search_string, search_ip)
    Search.add(newSearch)
    return make_response(jsonify({"success": True, 'msg': "add a search"}))