#!/usr/bin/env python3
"""Test for file_storage"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


class FileStorageTest(unittest.TestCase):
    """File_storage test"""

    def test_saveModel(self):
        """Test serialization and deserialization of
        BaseModel instance"""
        model = BaseModel()
        model.save()
        storage.all().clear()
        storage.reload()
        new_model = storage.all()[f'BaseModel.{model.id}']
        self.assertEqual(new_model.to_dict(), model.to_dict())

    def test_saveUser(self):
        """Test serialization and deserialization of
        User instance"""
        user = User()
        user.first_name = 'Ebube'
        user.last_name = 'Chukwuma'
        user.email = 'ebube@chukwuma.com'
        user.password = 'root'
        user.save()
        storage.all().clear()
        storage.reload()
        new_user = storage.all()[f'User.{user.id}']
        self.assertEqual(new_user.to_dict(), user.to_dict())

    def test_saveState(self):
        """Test serialization and deserialization of
        State instance"""
        state = State()
        state.name = 'Anambra'
        state.save()
        storage.all().clear()
        storage.reload()
        new_state = storage.all()[f'State.{state.id}']
        self.assertEqual(new_state.to_dict(), state.to_dict())

    def test_saveCity(self):
        """Test serialization and deserialization of
        City instance"""
        city = City()
        city.state_id = 'ET24B'
        city.name = 'Awka-Etiti'
        city.save()
        storage.all().clear()
        storage.reload()
        new_city = storage.all()[f'City.{city.id}']
        self.assertEqual(new_city.to_dict(), city.to_dict())

    def test_saveAmenity(self):
        """Test serialization and deserialization of Amenity instance"""
        amenity = Amenity()
        amenity.name = 'car'
        amenity.save()
        storage.all().clear()
        storage.reload()
        new_amenity = storage.all()[f'Amenity.{amenity.id}']
        self.assertEqual(new_amenity.to_dict(), amenity.to_dict())

    def test_savePlace(self):
        """Test serialization and deserialization of Place instance"""
        place = Place()
        place.city_id = 'AWK21'
        place.user_id = 'EB45'
        place.name = 'Lagos'
        place.desctription = 'A very beautiful place'
        place.number_rooms = 5
        place.number_bathrooms = 4
        place.max_guest = 3
        place.price_by_night = 50000
        place.latitude = 5.3
        place.longitute = 9.5
        place.amenity_ids = ['ab23', 'a56ty', 'yh57', 'm68jh']
        place.save()
        storage.all().clear()
        storage.reload()
        new_place = storage.all()[f'Place.{place.id}']
        self.assertEqual(new_place.to_dict(), place.to_dict())

    def test_saveReview(self):
        """Test serialization and deserialization of Review instance"""
        review = Review()
        review.place_id = '89UJ'
        review.user_id = 'IU78'
        review.text = 'A nice place to stay'
        review.save()
        storage.all().clear()
        storage.reload()
        new_review = storage.all()[f'Review.{review.id}']
        self.assertEqual(new_review.to_dict(), review.to_dict())

if __name__ == '__main__':
    unittest.main()
