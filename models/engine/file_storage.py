#!/usr/bin/python3
"""this module is for magnament of storage of data
    classes:
        FileStorage
"""
import os
import json


class FileStorage():
    """ this class admint the data storage
        instances:
            __file_path, __objects
        methods:
            all, new, save, reload
    """
    __file_path = "/home/vagrant/arbn_prev/file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return (self.reload())

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        value = obj.to_dict()
        self.__objects[key] = value
        return self.__objects

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.isfile(self.__file_path):
            filesize = os.path.getsize(self.__file_path)
            if filesize:
                with open(self.__file_path, 'r') as file:
                    self.__objects = json.load(file)
            else:
                self.__objects = {}
        return (self.__objects)
