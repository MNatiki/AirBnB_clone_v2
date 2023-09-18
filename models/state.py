#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, ForeignKey
from models.base_model import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship('City', backref='state', cascade="all, delete")
    else:
        @property
        def cities(self):
            from models import storage
            all_obj = storage.all()
            return [i for i in all_obj.keys()
                    if all_obj[i].__class__ == 'City'
                    and all_obj[i].state_id == self.state_id]
