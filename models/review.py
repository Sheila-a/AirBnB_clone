#!/usr/bin/env python3
'''Module that defines the class Review'''


from .base_model import BaseModel


class Review(BaseModel):
    '''inherits BaseModel with added properties'''
    place_id = ''
    user_id = ''
    text = ''
