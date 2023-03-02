#!/usr/bin/python3
"""

"""

import json


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
        """ Deserializes the JSON file to __objetcs.
            """
        from ..amenity import Amenity
        from ..base_model import BaseModel
        from ..city import City
        from ..place import Place
        from ..review import Review
        from ..state import State
        from ..user import User

        try:
            with open(self.__file_path, mode='r') as jsonfile:
                file_objects = json.load(jsonfile).items()
                for key, value in file_objects:
                    eval(value["__class__"])(**value)
        except Exception:
            return
