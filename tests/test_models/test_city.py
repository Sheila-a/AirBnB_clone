#!/usr/bin/env python3
"""test for city"""
import unittest
from models.city import City
from models.base_model import BaseModel


class CityTest(unittest.TestCase):
    """City test"""
    def test_creation(self):
        """checks that instance can be created with appropraite values"""
        my_city = City()
        my_city.name = 'house'
        my_city.state_id = '25GH'
        self.assertIsNotNone(my_city)
        class_type = "<class 'models.city.City'>"
        self.assertEqual(str(type(my_city)), class_type)
        self.assertIsInstance(my_city, City)
        self.assertTrue(issubclass(type(my_city), BaseModel))

    def test_todict(self):
        """checks the dictionary rep of a BaseModel
        instance"""
        my_city = City()
        model_dict = {'id': my_city.id}
        created_at = my_city.created_at.isoformat()
        updated_at = my_city.updated_at.isoformat()
        model_dict['created_at'] = created_at
        model_dict['updated_at'] = updated_at
        model_dict['__class__'] = 'City'
        self.assertEqual(model_dict, my_city.to_dict())

    def test_serialisation(self):
        """checks for serialisation of object"""
        my_city = City()
        my_city.name = "My_First_Model"
        model_dict = my_city.to_dict()
        new_city = City(**model_dict)
        self.assertEqual(new_city.to_dict(), my_city.to_dict())
        self.assertIn('__class__', new_city.to_dict())
        self.assertNotIn('__class__', new_city.__dict__)
        class_type = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(new_city.created_at)), class_type)
        self.assertEqual(str(type(new_city.updated_at)), class_type)
        self.assertIsNot(my_city, new_city)


if __name__ == '__main__':
    unittest.main()
