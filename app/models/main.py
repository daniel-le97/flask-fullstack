from flask_login import UserMixin
from app import db

class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship("Book", backref="author")

def __repr__(self: Author) -> str:
    return '<Author: {}>'.format(self.books)

class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.author_id"))
    title = db.Column(db.String)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)