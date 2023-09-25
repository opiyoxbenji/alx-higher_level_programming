#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Except as e:
        sys.stderr.write("Except: {}\n".format(e))
        result = None
    return result

def my_function(a, b):
    return a / b

result1 = safe_function(my_function, 10, 2)
result2 = safe_function(my_function, 10, 2)
print(result1, result2)
