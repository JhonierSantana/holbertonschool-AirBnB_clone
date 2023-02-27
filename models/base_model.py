#!/usr/bin/python3
from datetime import datetime
import models
import uuid


class BaseModel:
    def Base(self, id):
        self.id = id
        id = uuid.uuid4()
        self.id = str(id)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,\
            self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
    