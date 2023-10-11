#!/usr/bin/python3
"""Defines a JSON representation of an object"""
import json


def to_json_string(my_obj):
    """ Returns the JSON representation of an object as a string"""
    return json.dumps(my_obj)
