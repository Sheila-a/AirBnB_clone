#!/usr/bin/env python3
"""test for state"""
import unittest
from models.state import State
from models.base_model import BaseModel


class StateTest(unittest.TestCase):
    """State test"""
    def test_creation(self):
        """checks that instance can be created with appropraite values"""
        my_state = State()
        my_state.name = 'Abia'
        self.assertIsNotNone(my_state)
        class_type = "<class 'models.state.State'>"
        self.assertEqual(str(type(my_state)), class_type)
        self.assertIsInstance(my_state, State)
        self.assertTrue(issubclass(type(my_state), BaseModel))

    def test_todict(self):
        """checks the dictionary rep of a BaseModel
        instance"""
        my_state = State()
        model_dict = {'id': my_state.id}
        created_at = my_state.created_at.isoformat()
        updated_at = my_state.updated_at.isoformat()
        model_dict['created_at'] = created_at
        model_dict['updated_at'] = updated_at
        model_dict['__class__'] = 'State'
        self.assertEqual(model_dict, my_state.to_dict())

    def test_serialisation(self):
        """checks for serialisation of object"""
        my_state = State()
        my_state.name = "My_First_Model"
        model_dict = my_state.to_dict()
        new_state = State(**model_dict)
        self.assertEqual(new_state.to_dict(), my_state.to_dict())
        self.assertIn('__class__', new_state.to_dict())
        self.assertNotIn('__class__', new_state.__dict__)
        class_type = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(new_state.created_at)), class_type)
        self.assertEqual(str(type(new_state.updated_at)), class_type)
        self.assertIsNot(my_state, new_state)


if __name__ == '__main__':
    unittest.main()
