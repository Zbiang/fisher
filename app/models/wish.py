from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, SmallInteger
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from app.models.base import db, Base


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('User')
    # bid = Column(Integer, ForeignKey('user.id'))
    launched = Column(Boolean, default=False)
