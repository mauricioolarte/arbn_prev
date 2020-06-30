#!/usr/bin/python3
""" this module content the class amenety
    atributes:
        name
"""

from models import storage
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ this class is amenity """

    name = ""
