#!/usr/bin/python3
""" this module content the class amenety
    atributes:
        text, user_id, place_id
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ classes that inherit from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
