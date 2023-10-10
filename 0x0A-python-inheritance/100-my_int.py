#!/usr/bin/python3
"""Defines a class that inherits from  int"""


class MyInt(int):
    """Invert in operators == and !="""

    def __eq__(self, value):
        """Overrides == operator with !="""
        return self.real != value

    def __no__(self, value):
        """Overrides != operator with =="""
        return self.real == value
