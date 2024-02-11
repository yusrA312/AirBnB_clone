#!/usr/bin/python3
"""This is the base class"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """Base"""

    def __init__(self, *myargs, **mykwargs):
        """init"""
        ISO = "%Y-%m-%dT%H:%M:%S.%f"
        if mykwargs is not None and mykwargs != {}:
            for key, value in mykwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, ISO)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """save method"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """To dict method"""
        ISO = "%Y-%m-%dT%H:%M:%S.%f"

        iso_format_keys = {"created_at", "updated_at"}

        dict_copy = {
            key: value.isoformat()
            if key in iso_format_keys and hasattr(value, "isoformat")
            else value
            for key, value in self.__dict__.items()
        }
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy

    def __str__(self):
        """__str__ method"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
