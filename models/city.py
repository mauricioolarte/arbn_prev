#!/usr/bin/python3
""" this module content the class amenety
    atributes:
        text, user_id, place_id
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ classes that inherit from BaseModel"""
    state_id = ""
    name = ""
