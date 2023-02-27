#!/usr/bin/python3
from datetime import datetime
import models
import uuid

class BaseModel:
    """
    BaseModel that defines all common attributes/methods for other classes
    PUBLIC INSTANCE ATTRIBUTES:
    id string - assign with an uuid when an instance is created
        uuid.uuid4(): generate a unique id but cant forget to
        convert to string. The goal is to have a unique id for each BaseModel
    created_at: datetime - assign with the current datetime when an instance
        is created
    update_at: datetime - assign with the current datetime when an instance
        is created and it will be update every time you change your
        object
    __str__: should print: [<class name>] (<self.id>) <self.__dict__>
    PUBLIC INSTANCE METHODS
    save(self):
    to_dict(self):
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs.pop("__class__", None)
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
            else:
                setattr(self, key, value)
                
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,\
            self.id, self.__dict__)
        
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()
        
    def to_dict(self):
        dict1 = dict()
        for (key, value) in (self.__init__).items:
            if isinstance(value, datetime):
                dict1[key] = value.isoformat()
            else:
                dict1[key] = value
        dict1["__class__"] = self.__class__.__name__
        return(dict1)
