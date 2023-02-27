#!/usr/bin/python3
import uuid
import models
from datetime import datetime
from os import path


class BaseModel:
    def Base(self, id):
        self.id = id
        id = uuid.uuid4()
        self.id_string = str(id)
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def __str__(self):
        return ([BaseModel]({}).format(self.id, self.__dict__))
    
    @property
    def updated_at(self):
        return self.__updated_at
    
    @updated_at.setter
    def updated_at(self, valor):
        self.__updated_at = datetime.now()
        
    def save(self):
        self.updated_at = datetime.now()