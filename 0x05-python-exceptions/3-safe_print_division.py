#!/usr/bin/python3
def safe_print_division(a, b):
    equal = 0

    try:
        equal = a / b
    except ZeroDivisionError:
        equal = None
    finally:
        print("Inside result: {}".format(equal))
        return equal
