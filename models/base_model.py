#!/usr/bin/env python3
"""This module defines the class BaseModel"""


import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """This class  defines all common attributes/methods
    for other classes"""

    def __init__(self, *args, **kwargs):
        if kwargs != {}:
            for i in kwargs.keys():
                if i != "__class__":
                    if i in ["created_at", "updated_at"]:
                        value = datetime.fromisoformat(kwargs[i])
                        self.__dict__[i] = value
                    else:
                        self.__dict__[i] = kwargs[i]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """string representation of an instance of
        BaseModel"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """saves this instance of the BaseModel"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Dictionary representation of an instance of
        BaseModel"""
        dict_rep = {**self.__dict__}
        dict_rep['__class__'] = type(self).__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
