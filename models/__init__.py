#!/usr/bin/python3
"""
module for init FileStorage
To create a unique FileStorage instance for the application importing
FileStorage, creating the variable storage (as instance of FileStorage)
and calling reload() method on this variable
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
