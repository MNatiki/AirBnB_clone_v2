#!/usr/bin/python3
"""
The `Place` class represents a place to stay
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from os import getenv
from models import storage
from models.review import Review


class Place(BaseModel, Base):
    """
    The `Place` class represents a place to stay with
    various attributes such as name, description,
    number of rooms, number of bathrooms,
    maximum number of guests, price per night, latitude,
    longitude, and a list of amenity IDs.
    """
    __tablename__ = "places"
    city_id = Column(String(60),
                     ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review',
                               backref='place', cascade="all, delete")
    else:
        @property
        def reviews(self):
            """
            The function "reviews" returns a list of reviews
            associated with a specific place.
            """
            my_list = []
            for i in storage.all(Review).values():
                if i.place_id == self.id:
                    my_list.append(i)
            return my_list
