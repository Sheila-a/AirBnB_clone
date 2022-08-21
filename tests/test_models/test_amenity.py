#!/usr/bin/env python3
"""test for amenity"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class AmenityTest(unittest.TestCase):
    """Amenity test"""
    def test_creation(self):
        """checks that instance can be created with appropraite values"""
        my_amenity = Amenity()
        my_amenity.name = 'house'
        self.assertIsNotNone(my_amenity)
        class_type = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(my_amenity)), class_type)
        self.assertIsInstance(my_amenity, Amenity)
        self.assertTrue(issubclass(type(my_amenity), BaseModel))

    def test_todict(self):
        """checks the dictionary rep of a BaseModel
        instance"""
        my_amenity = Amenity()
        model_dict = {'id': my_amenity.id}
        created_at = my_amenity.created_at.isoformat()
        updated_at = my_amenity.updated_at.isoformat()
        model_dict['created_at'] = created_at
        model_dict['updated_at'] = updated_at
        model_dict['__class__'] = 'Amenity'
        self.assertEqual(model_dict, my_amenity.to_dict())

    def test_serialisation(self):
        """checks for serialisation of object"""
        my_amenity = Amenity()
        my_amenity.name = "My_First_Model"
        model_dict = my_amenity.to_dict()
        new_amenity = Amenity(**model_dict)
        self.assertEqual(new_amenity.to_dict(), my_amenity.to_dict())
        self.assertIn('__class__', new_amenity.to_dict())
        self.assertNotIn('__class__', new_amenity.__dict__)
        class_type = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(new_amenity.created_at)), class_type)
        self.assertEqual(str(type(new_amenity.updated_at)), class_type)
        self.assertIsNot(my_amenity, new_amenity)


if __name__ == '__main__':
    unittest.main()
