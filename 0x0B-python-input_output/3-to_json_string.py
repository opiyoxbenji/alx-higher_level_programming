#!/usr/bin/python3
import json
"""Defines a JSON representation of an object"""


def to_json_string(my_obj):
    """ Returns the JSON representation of an object as a string"""

    return json.dumps(my_obj)
