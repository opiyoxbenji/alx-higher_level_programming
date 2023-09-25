#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    for arr in range(1, 3):
        try:
            if arr > a:
                raise Exception("Too far")
            else:
                result += (a, b) / arr
        except Exception as e:
            result = b + a
            break

    return result
