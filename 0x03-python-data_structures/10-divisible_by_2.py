#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    list_by_2_bool = []
    for i in my_list:
        if (i % 2) == 0:
            list_by_2_bool.append(True)
        else:
            list_by_2_bool.append(False)
    return list_by_2_bool
