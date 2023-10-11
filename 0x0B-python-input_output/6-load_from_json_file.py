#!/usr/bin/python3
"""Defines a JSON representation of an object"""
import json


def load_from_json_file(filename):
    """Loads an object from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        loaded_obj = json.load(file)

    return loaded_obj
