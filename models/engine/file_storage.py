#!/usr/bin/python3

import json


class FileStorage():
    __file_path = "/home/vagrant/arbn_prev/file.json"
    __objects = {}
    

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        value = obj.to_dict()
        self.__objects[key] = value
        return self.__objects

    def save(self):
        dic = {}
        for id, obj in self.__objects.items():
            dic[id] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(dic, file)
    
    def reload(self):
        with open(self.__file_path, 'r') as file:
            obj = json.load(file)
        for key, value in obj.items():
            name = models.classes[value["__class__"]](**value)
            self.__objects[key] = value
