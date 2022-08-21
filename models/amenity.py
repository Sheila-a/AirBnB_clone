#!/usr/bin/env python3
'''Module that defines the class Amenity'''


from .base_model import BaseModel


class Amenity(BaseModel):
    '''inherits BaseModel with added properties'''
    name = ''
