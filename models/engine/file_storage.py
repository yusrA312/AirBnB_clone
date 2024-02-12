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
            with open(self.__file_path, "r", encoding="UTF8") as file:
                loaded_dict = json.load(file)
                self.__objects = {}
                for key, value in loaded_dict.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        cls = BaseModel
                    else:
                        cls = getattr(models, class_name)
                    instance = cls(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
