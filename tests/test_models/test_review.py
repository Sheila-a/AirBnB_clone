#!/usr/bin/env python3
"""test for review"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class ReviewTest(unittest.TestCase):
    """Review test"""
    def test_creation(self):
        """checks that instance can be created with appropraite values"""
        my_review = Review()
        my_review.place_id = 'house'
        self.assertIsNotNone(my_review)
        class_type = "<class 'models.review.Review'>"
        self.assertEqual(str(type(my_review)), class_type)
        self.assertIsInstance(my_review, Review)
        self.assertTrue(issubclass(type(my_review), BaseModel))

    def test_todict(self):
        """checks the dictionary rep of a BaseModel
        instance"""
        my_review = Review()
        model_dict = {'id': my_review.id}
        created_at = my_review.created_at.isoformat()
        updated_at = my_review.updated_at.isoformat()
        model_dict['created_at'] = created_at
        model_dict['updated_at'] = updated_at
        model_dict['__class__'] = 'Review'
        self.assertEqual(model_dict, my_review.to_dict())

    def test_serialisation(self):
        """checks for serialisation of object"""
        my_review = Review()
        my_review.name = "My_First_Model"
        model_dict = my_review.to_dict()
        new_review = Review(**model_dict)
        self.assertEqual(new_review.to_dict(), my_review.to_dict())
        self.assertIn('__class__', new_review.to_dict())
        self.assertNotIn('__class__', new_review.__dict__)
        class_type = "<class 'datetime.datetime'>"
        self.assertEqual(str(type(new_review.created_at)), class_type)
        self.assertEqual(str(type(new_review.updated_at)), class_type)
        self.assertIsNot(my_review, new_review)


if __name__ == '__main__':
    unittest.main()
