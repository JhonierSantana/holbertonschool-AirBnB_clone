#!/usr/bin/python3
""" class Base Model """

from datetime import datetime
import uuid


class BaseModel():

    """
    BaseModel that defines all common attributes/methods for other classes
    PUBLIC INSTANCE ATTRIBUTES:
    id string - assign with an uuid when an instance is created
        uuid.uuid4(): generate a unique id but cant forget to
        convert to string. The goal is to have a unique id for each
        BaseModel
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
        """initialization"""
        from models import storage
        if kwargs:
            kwargs.pop("__class__", None)
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime
                            (value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """__str__ method should print"""
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        This method will be the first piece of the serialization/
        deserialization process: create a dictionary representation
        with simple object type of our BaseModel
        """
        dict1 = dict(self.__dict__)
        dict1["__class__"] = type(self).__name__
        dict1["created_at"] = dict1["created_at"].isoformat()
        dict1["updated_at"] = dict1["updated_at"].isoformat()
        return dict1
