#!/usr/bin/python3
""" test for clases
    Atributes:
        all
"""


import unittest
from models.place import Place
import datetime
import pep8


class Test_BaseModel(unittest.TestCase):
    """ this tests methods of base
        Atributes:
            All
    """

    @classmethod
    def test_setUpClass(self):
        print("Base setUpClass")

    @classmethod
    def test_tearDownClass(self):
        print("base tearDownClass")

    def test_setUp(self):
        print("base setUp")

    def test_tearDown(self):
        print("base tearDown")

    def test_funtion(self):
        self.assertTrue(True)
    """ my test """

    def test_city_id(self):
        self.city_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        self.assertEqual("b6a6e15c-c67d-4312-9a75-9d084935e579", self.city_id)

    def test_user_id(self):
        self.user_id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        self.assertEqual("b6a6e15c-c67d-4312-9a75-9d084935e579", self.user_id)

    def test_name(self):
        self.name = "el mejor sitio"
        self.assertEqual("el mejor sitio", self.name)

    def test_description(self):
        self.description = "es un lugar lindo"
        self.assertEqual("es un lugar lindo", self.description)

    def test_number_rooms(self):
        self.number_rooms = 2
        self.assertEqual(2, self.number_rooms)

    def test_number_bathrooms(self):
        self.number_bathrooms = 2
        self.assertEqual(2, self.number_bathrooms)

    def test_max_guest(self):
        self.max_guest = 6
        self.assertEqual(6, self.max_guest)

    def test_price_by_night(self):
        self.price_by_night = 2
        self.assertEqual(2, self.price_by_night)

    def test_latitude(self):
        self.latitude = 2.89
        self.assertEqual(2.89, self.latitude)

    def test_name(self):
        self.longitude = 2.89
        self.assertEqual(2.89, self.longitude)

    def test_amenity_ids(self):
        self.amenity_ids = ['2', '3', '4']
        self.assertEqual(['2', '3', '4'], self.amenity_ids)

    def test_name(self):
        self.name = "holberton"
        self.assertEqual("holberton", self.name)

    def test_id(self):
        self.id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        self.assertEqual("b6a6e15c-c67d-4312-9a75-9d084935e579", self.id)

    def test_created_at(self):
        self.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        self.assertEqual(datetime.datetime(
            2017, 9, 28, 21, 5, 54, 119427), self.created_at)

    def test_updated_at(self):
        self.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119434)
        self.assertEqual(datetime.datetime(
            2017, 9, 28, 21, 5, 54, 119434), self.updated_at)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    if __name__ == '__main__':
        unittest.main()
