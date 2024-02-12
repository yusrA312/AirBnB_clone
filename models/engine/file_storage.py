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
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """SAVE"""
        jno = {}
        for key in self.__objects:
            jno[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w") as F:
            json.dump(jno, F)

    def reload(self):
        """Reloads objects from JSON file"""
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                for key, value in json.load(f).items():
                    att_value = eval(value["__class__"])(**value)
                    self.__objects[key] = att_value
        except FileNotFoundError:
            pass
