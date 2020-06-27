#!/usr/bin/python3

import json


class FileStorage():
    __file_path = "/home/vagrant/arbn_borrador/file.json"
    __objects = {}
    

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + obj.id
        value = obj.to_dict()
        self.__objects[key] = value
        return self.__objects

    def save(self):
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)
    
    def reload(self):
        with open(self.__file_path, 'r') as file:
            self.__objects = json.load(file)
