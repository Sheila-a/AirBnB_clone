#!/usr/bin/env python3
"""Module for base model"""
import unittest
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """Base model tests"""

    def test_creation(self):
        """Checks that an instance can be created with
        appropriate values"""
        my_model = BaseModel()
        self.assertIsNotNone(my_model)
        self.assertIsNotNone(my_model.id)

    def test_str(self):
        """checks the string representation of a class"""
        my_model = BaseModel()
        id = my_model.id
        strn = f'[BaseModel] ({id}) {my_model.__dict__}'
        self.assertEqual(strn, my_model.__str__())

    def test_todict(self):
        """checks the dictionary rep of a BaseModel
        instance"""
        my_model = BaseModel()
        model_dict = {'id': my_model.id}
        created_at = my_model.created_at.isoformat()
        updated_at = my_model.updated_at.isoformat()
        model_dict['created_at'] = created_at
        model_dict['updated_at'] = updated_at
        model_dict['__class__'] = 'BaseModel'
        self.assertEqual(model_dict, my_model.to_dict())

    def test_serialisation(self):
        """checks for serialisation of object"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        model_dict = my_model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.to_dict(), my_model.to_dict())
        self.assertIn('__class__', new_model.to_dict())
        self.assertNotIn('__class__', new_model.__dict__)
        class_type = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(new_model.created_at)), class_type)
        self.assertEqual(str(type(new_model.updated_at)), class_type)
        self.assertIsNot(my_model, new_model)


if __name__ == '__main__':
    unittest.main()
