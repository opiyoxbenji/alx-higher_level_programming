#!/usr/bin/python3
"""Defines a JSON representation of an object"""
import json


def class_to_json(obj):
    """Returns a dictionary description"""
    serializable_dict = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value

    return serializable_dict
