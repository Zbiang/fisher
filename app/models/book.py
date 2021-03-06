from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

from app.models.base import db, Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    _password = Column('password', String(64))
    price = Column(String(20))
    pages = Column(Integer)
    pudate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))