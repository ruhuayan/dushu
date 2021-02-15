"""Data models."""
from . import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Book(db.Model):
    __tablename__ = "books"
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

class BookSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Book
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    href = fields.String(required=True)
    author = fields.String(required=True)
    category = fields.String(required=True)
    alphabet = fields.String(required=True)
    created_at = fields.DateTime()

class Chapter(db.Model):
    __tablename__ = "chapters"
    chapter_id = db.Column(db.Integer, primary_key=True, autoincrement=False,)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True, autoincrement=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime())
    # book = db.relationship("Book", backref='book', lazy=True)
    def __repr__(self):
        return f'<Book {self.book_id} - Chapter {self.title}>'

class ChapterSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Chapter
        sqla_session = db.session
    chapter_id = fields.Number(required=True)
    book_id = fields.Number(required=True)
    title = fields.String(required=True)
    content = fields.String()
    created_at = fields.DateTime()

class Serie(db.Model):
    __tablename__ = "series"
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    serie_title = db.Column(db.String(255), nullable=False)
    href = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime())
    def __repr__(self):
        return f'<Book {self.book_id} - Serie {self.serie_title}>'

class SerieSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Serie
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    book_id = fields.Number(required=True)
    serie_title = fields.String(required=True)
    href = fields.String(required=True)