#!/usr/bin/env python3
'''Module that defines the class City'''


from .base_model import BaseModel


class City(BaseModel):
    '''inherits BaseModel with added properties'''
    state_id = ''
    name = ''
