#!/usr/bin/python3
"""Defines a JSON representation of an object"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
