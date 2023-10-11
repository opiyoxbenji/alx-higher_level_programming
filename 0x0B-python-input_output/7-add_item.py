#!/usr/bin/python3
"""Adds all arguments to a Python list"""
import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Get the command-line arguments excluding the script name
arguments = sys.argv[1:]

# Initialize an empty list
my_list = []

# Check if the "add_item.json" file exists
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    pass

# Add the command-line arguments to the list
my_list.extend(arguments)

# Save the updated list to "add_item.json"
save_to_json_file(my_list, "add_item.json")
