#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    copy = my_list.copy()
    copy.sort(reverse=True)
    return copy[0]
