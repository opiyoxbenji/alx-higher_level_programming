#!/usr/bin/python3
"""Defines an object instance from a specified class"""


def inherits_from(obj, a_class):
    """Returns True if an object instance is from a specified directory"""

    return issubclass(type(obj), a_class) and type(obj) != a_class
