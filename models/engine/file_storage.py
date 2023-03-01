#!/usr/bin/python3
"""

"""

import json

class FileStorage:
    """
    
    """
    __file_path = "data.json"
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
        with open(self.__file_path, mode='w') as jsonfile:
            json.dump(new_dict, jsonfile)
    
    
    def reload(self):
        
        from ..base_model import BaseModel
        try:
            with open(self.__file_path, "r") as jsonfile:
                file_objects = json.load(jsonfile).items()
                for key, value in file_objects:
                    eval(value["__class__"](**value))
        except Exception:
            return