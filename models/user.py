#!/usr/bin/env python3
"""Module that defines the class User"""


from .base_model import BaseModel


class User(BaseModel):
    """Class that models a user"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
