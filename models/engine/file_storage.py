#!/usr/bin/python3
"""

"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from os import path

class FileStorage():
    """
    
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        key =  ("{}.{}".format(self.__class__.__name__, obj.id))
        self.__objects[key] = obj
        
        
    def save(self):
        """ Serializes __objetcs to a JSON file.
            """
        new_dict = {}
        for (key, value) in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as jsonfile:
            json.dump(new_dict, jsonfile)
    
    
    def reload(self):
        """
        This method loads the dictionary of objects from the JSON file.
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as fl:
                json_data = json.load(fl)
                for i in json_data.values():
                    class_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(class_name)(**i))
        else:
            pass
