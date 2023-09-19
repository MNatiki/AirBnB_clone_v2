#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Review(BaseModel, Base):
    """
    Review class to store review information
    The Review class is used to store review information,
    including the place ID, user ID, and text of
    the review.
    """
    __tablename__ = 'reviews'
    place_id = Column(String(60),
                      ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
