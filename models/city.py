#!/usr/bin/python3
"""
City Module for HBNB project
#The City class represents a city and contains
its name and state ID.
"""
from models.base_model import BaseModel, Base, ForeignKey
from models.base_model import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
     The city class, contains state ID and name
     The City class represents a city and contains
     its name and state ID.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'),
                      nullable=False)
    places = relationship('Place', backref='cities', cascade="all, delete")
