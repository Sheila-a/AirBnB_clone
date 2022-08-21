#!/usr/bin/env python3
"""test for place"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class PlaceTest(unittest.TestCase):
    """Place test"""
    def test_creation(self):
        """checks that instance can be created with appropraite values"""
        my_place = Place()
        my_place.name = 'house'
        my_place.user_id = '25GH'
        self.assertIsNotNone(my_place)
        class_type = "<class 'models.place.Place'>"
        self.assertEqual(str(type(my_place)), class_type)
        self.assertIsInstance(my_place, Place)
        self.assertTrue(issubclass(type(my_place), BaseModel))

    def test_todict(self):
        """checks the dictionary rep of a BaseModel
        instance"""
        my_place = Place()
        model_dict = {'id': my_place.id}
        created_at = my_place.created_at.isoformat()
        updated_at = my_place.updated_at.isoformat()
        model_dict['created_at'] = created_at
        model_dict['updated_at'] = updated_at
        model_dict['__class__'] = 'Place'
        self.assertEqual(model_dict, my_place.to_dict())

    def test_serialisation(self):
        """checks for serialisation of object"""
        my_place = Place()
        my_place.name = "My_First_Model"
        model_dict = my_place.to_dict()
        new_place = Place(**model_dict)
        self.assertEqual(new_place.to_dict(), my_place.to_dict())
        self.assertIn('__class__', new_place.to_dict())
        self.assertNotIn('__class__', new_place.__dict__)
        class_type = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(new_place.created_at)), class_type)
        self.assertEqual(str(type(new_place.updated_at)), class_type)
        self.assertIsNot(my_place, new_place)


if __name__ == '__main__':
    unittest.main()
