#!/usr/bin/python3
"""engine model"""


import json
from models.base_model import BaseModel
import models
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all"""
        return self.__objects

    def new(self, obj):
        """new"""
        key = obj.__class__.__name__ + "." + (obj.id)
        self.__objects[key] = obj

    def save(self):
        """SAVE"""
        jno = {}
        for key in self.__objects:
            jno[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w") as F:
            json.dump(jno, F)

    def reload(self):
        """reload"""
        try:
            with open(self.__file_path, "r", encoding="UTF8") as F:
                ES = json.load(F)
                self.__objects = {
                    key: eval(value["__class__"])(**value)
                    for key, value in ES.items()
                }
        except FileNotFoundError:
            pass
