#!/usr/bin/env python3
"""Init file for the package models"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
