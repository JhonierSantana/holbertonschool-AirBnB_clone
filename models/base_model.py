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
    def Base(self, id):
        self.id = id
        id = uuid.uuid4()
        self.id_string = str(id)
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def __str__(self):
        return ([BaseModel]({}).format(self.id, self.__dict__))
        
    def save(self):
        self.updated_at = datetime.now()
