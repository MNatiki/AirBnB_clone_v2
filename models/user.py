#!/usr/bin/python3
"""
This module defines a class User
The User class defines a user with attributes such as email,
password, first name, and last name.
"""
from models.base_model import BaseModel, Base
from models.base_model import Column, String, Integer
from sqlalchemy.orm import relationship
from models.review import Review


class User(BaseModel, Base):
    """
    This class defines a user by various attributes
    The User class defines a user with attributes
    such as email, password, first name, and last name.
    """

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship('Place',
                          backref='user', cascade="all, delete")
    reviews = relationship("Review", backref='user', cascade="all, delete")
