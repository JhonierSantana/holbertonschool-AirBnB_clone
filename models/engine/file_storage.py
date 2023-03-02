#!/usr/bin/python3
""" FileStorage class """
import json
from models.base_model import BaseModel
import datetime
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file
    to instances.
    ATTRIBUTES:
    __file_path is a private class attribute (str) path to the JSON file
    __objects is a private class attribute (dict) that is empty but will
    store all objects by <class name>.id ex: to store a BaseModel object
    with id=12121212, the key will be BaseModel.12121212)
    PUBLIC INSTANCE METHODS
    all():
    new(obj):
    save():
    reload():
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all method that returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ new method sets in __objects the obj with
        key <obj class name>.id """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """ save method serializes __objects to the JSON file
        (path: __file_path) """
        with open(FileStorage.__file_path, encoding='utf-8', mode='w') as file:
            new_d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(new_d, file)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn't exist,
        no exception should be raised) """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
