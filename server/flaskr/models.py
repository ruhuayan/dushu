"""Data models."""
from . import db, ma

class Book(db.Model):
    __tablename__ = "books"
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    href = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    alphabet = db.Column(db.String(1), nullable=False)
    description = db.Column(db.Text)
    download_ebook_count = db.Column(db.Integer)
    download_pdf_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime())

    def download_ebook(id):
        book_to_update = Book.query.filter_by(id=id).first()
        book_to_update.download_ebook_count += 1
        db.session.commit()
        return book_to_update.download_ebook_count

    def download_pdf(id):
        book_to_update = Book.query.filter_by(id=id).first()
        book_to_update.download_pdf_count += 1
        db.session.commit()
        return book_to_update.download_pdf_count

    def __repr__(self):
        return f'<Book {self.title}>'

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book

class Chapter(db.Model):
    __tablename__ = "chapters"
    __table_args__ = {'extend_existing': True} 
    chapter_id = db.Column(db.Integer, primary_key=True, autoincrement=False,)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True, autoincrement=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime())
    # book = db.relationship("Book", backref='book', lazy=True)
    def __repr__(self):
        return f'<Book {self.book_id} - Chapter {self.title}>'

class ChapterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Chapter

class Serie(db.Model):
    __tablename__ = "series"
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    serie_id = db.Column(db.Integer, nullable=False)
    serie_title = db.Column(db.String(255), nullable=False)
    href = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime())
    def __repr__(self):
        return f'<Book {self.book_id} - Serie {self.serie_title}>'

class SerieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Serie

class Search(db.Model):
    __tablename__ = "search"
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(50), nullable=False)
    ip = db.Column(db.String(50), nullable=False)
    # created_at = db.Column(db.DateTime())

    def __init__(self, query, ip):
        self.query = query
        self.ip = ip

    def add(newSearch):
        db.session.add(newSearch)   
        db.session.commit()