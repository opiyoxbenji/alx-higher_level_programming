#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_values = set()
    result = 0

    for item in my_list:
        if item not in unique_values:
            result += item
            unique_values.add(item)

    return result
