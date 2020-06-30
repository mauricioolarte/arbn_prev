#!/usr/bin/python3
""" this module content the class amenety
    atributes:
        text, user_id, place_id
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ this class is Review """

    place_id = ""
    user_id = ""
    text = ""
