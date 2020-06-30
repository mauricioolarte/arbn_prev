#!/usr/bin/python3
""" test for clases
    Atributes:
        all
"""


import unittest
from models.state import State
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

    def test_dict(self):
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
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    if __name__ == '__main__':
        unittest.main()
