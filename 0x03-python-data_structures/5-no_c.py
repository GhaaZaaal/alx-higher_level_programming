#!/usr/bin/python3
def no_c(my_string):
    for i in range(0, len(my_string) + 1):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_string = my_string[i]

    return new_string
