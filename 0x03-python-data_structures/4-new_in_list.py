#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    len_t = len(my_list)

    if idx < 0 or idx >= len_t:
        return my_list.copy()

    new_list = list(my_list)
    new_list[idx] = element

    return new_list
