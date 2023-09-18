#!/usr/bin/python3
"""
This module defines a class User
The User class defines a user with attributes such as email,
password, first name, and last name.
"""
from models.base_model import BaseModel, Base
from models.base_model import Column, String, Integer


class User(BaseModel, Base):
    """
    This class defines a user by various attributes
    The User class defines a user with attributes
    such as email, password, first name, and last name.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
