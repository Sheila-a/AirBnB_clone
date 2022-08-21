#!/usr/bin/env python3
"""test for user"""
import unittest
from models.user import User
from models.base_model import BaseModel


class UserTest(unittest.TestCase):
    """User test"""
    def test_creation(self):
        """checks that instance can be created with appropraite values"""
        my_user = User()
        my_user.first_name = 'Nmesoma'
        my_user.last_name = 'Udojike'
        my_user.email = 'udojyk@gmail.com'
        self.assertIsNotNone(my_user)
        class_type = "<class 'models.user.User'>"
        self.assertEqual(str(type(my_user)), class_type)
        self.assertIsInstance(my_user, User)
        self.assertTrue(issubclass(type(my_user), BaseModel))

    def test_todict(self):
        """checks the dictionary rep of a BaseModel
        instance"""
        my_user = User()
        model_dict = {'id': my_user.id}
        created_at = my_user.created_at.isoformat()
        updated_at = my_user.updated_at.isoformat()
        model_dict['created_at'] = created_at
        model_dict['updated_at'] = updated_at
        model_dict['__class__'] = 'User'
        self.assertEqual(model_dict, my_user.to_dict())

    def test_serialisation(self):
        """checks for serialisation of object"""
        my_user = User()
        my_user.name = "My_First_Model"
        model_dict = my_user.to_dict()
        new_user = User(**model_dict)
        self.assertEqual(new_user.to_dict(), my_user.to_dict())
        self.assertIn('__class__', new_user.to_dict())
        self.assertNotIn('__class__', new_user.__dict__)
        class_type = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(new_user.created_at)), class_type)
        self.assertEqual(str(type(new_user.updated_at)), class_type)
        self.assertIsNot(my_user, new_user)


if __name__ == '__main__':
    unittest.main()
