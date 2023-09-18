#!/usr/bin/python3
from ..base_model import Base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
import MySQLdb
from .classes import classes


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        connect = MySQLdb.connect(host="localhost", port=3306,
                                  user="hbnb_dev", passwd="hbnb_dev_pwd",
                                  charset="utf8")
        cursor = connect.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS hbnb_dev_db")
        connect.commit()
        cursor.close()
        connect.close()
        self.__engine = create_engine('mysql+mysqldb://'
                                      '{}:{}@{}:3306/{}'.format(
                                          getenv('HBNB_MYSQL_USER'), getenv(
                                              'HBNB_MYSQL_PWD'),
                                          getenv('HBNB_MYSQL_HOST'), getenv(
                                              'HBNB_MYSQL_DB')
                                      ), pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        my_dict = {}
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if cls:
            my_query = self.__session.query(eval(cls)).all()
            for i in my_query:
                my_dict[str(my_query.__name__) + "." + i.id] = i
            print(my_query)
            return my_dict
        for key, value in classes.items():
            # print(f"{key} {value.id}")
            my_query = self.__session.query(value).all()
            for i in my_query:
                my_dict[str(key) + "." + i.id] = i
        print(my_query)
        return my_dict

    def new(self, obj):
        # print("passed new")
        # print(obj)
        self.__session.add(obj)
        print(self.__session.new)

    def save(self):
        # print("in db save")
        self.__session.commit()

    def delete(self, obj=None):
        if obj is None:
            return
        self.__session.delete(obj)

    def reload(self):
        from ..amenity import Amenity
        from ..city import City
        from ..place import Place
        from ..review import Review
        from ..state import State
        from ..user import User
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                        expire_on_commit=False))()
