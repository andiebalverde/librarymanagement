from myproject import db
from sqlalchemy.orm import column_property, relationship
from sqlalchemy import Column, Integer, String
import enum
from enum import IntEnum

class ActTypeEnum(IntEnum):
    Checkin = 1
    Checkout = 2
    Donate = 3
    Create = 4

class Users(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.name:
            return f"{self.name}"
        else:
            return f"User doesn't exist"


class LibraryActivities(db.Model):

    __tablename__ = 'library_activities'

    library_activity_id = db.Column(db.Integer,primary_key= True)
    #activity_type = db.Column(db.Enum(ActTypeEnum))
    activity_type = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    library_book_id = db.Column(db.Integer, db.ForeignKey("library_books.library_book_id"))
    checked_out_at = db.Column(db.DateTime, nullable=True)
    checked_in_at = db.Column(db.DateTime, nullable=True)

    def __init__(self,activity_type, user_id, library_book_id, checked_out_at, checked_in_at):
        self.activity_type = activity_type
        self.user_id = user_id
        self.library_book_id = library_book_id
        self.checked_out_at = checked_out_at
        self.checked_in_at = checked_in_at

    def __repr__(self):
        return f"Library Activity: library_activity_id: {self.library_activity_id}, activity_type: {self.activity_type}, " \
               f"user_id: {self.user_id}, library_book_id: {self.library_book_id}, checked_out_at: {self.checked_out_at}, " \
               f"checked_in_at: {self.checked_in_at}"

class Books(db.Model):

    __tablename__ = 'books'
    book_id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    author_name = db.Column(db.String(255), nullable=True)
    isdn_num = db.Column(db.String(255), nullable=True)
    genre = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, title, author_name, isdn_num, genre, description):

        self.title = title
        self.author_name = author_name
        self.isdn_num = isdn_num
        self.genre = genre
        self.description = description

    def __repr__(self):
        if self.title:
            return f"Title: {self.title}. Author: {self.author_name}, ISDN: {self.isdn_num}, Genre: {self.isdn_num}" \
                   f" Description: {self.description}"

class LibraryBooks(db.Model):

    __tablename__ = 'library_books'
    library_book_id = db.Column(db.Integer, primary_key=True)
    library_id = db.Column(db.Integer, db.ForeignKey("libraries.library_id"))
    book_id = db.Column(db.Integer,db.ForeignKey("books.book_id"))
    last_library_activity_id = db.Column(db.Integer, db.ForeignKey("library_activities.library_activity_id"), nullable=True)

    #Relationships:
    libraries = relationship("Libraries")
    library_activities = relationship("LibraryActivities", foreign_keys=last_library_activity_id)
    books = relationship("Books")

    def __init__(self, library_id, book_id, last_library_activity_id):
        self.library_id = library_id
        self.book_id = book_id
        self.last_library_activity_id = last_library_activity_id


    def __repr__(self):
        return f"Library Book ID: {self.library_book_id}, Library ID: {self.library_id}, Book ID: {self.book_id}, Last Library Activity ID: {self.last_library_activity_id} "


class Libraries(db.Model):

    __tablename__ = 'libraries'
    library_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String, nullable=True)
    state = db.Column(db.String, nullable=True)
    postal_code = db.Column(db.Text, nullable=True)

    library_books = relationship("LibraryBooks")
    #library_activities = relationship("LibraryActivities", primaryjoin=library_id)

    def __init__(self, name, city=None, state=None, postal_code=None):
        self.name = name
        self.city = city
        self.state = state
        self.postal_code = postal_code

    def __repr__(self):
        if self.name:
            return f"Library name is {self.name}"
