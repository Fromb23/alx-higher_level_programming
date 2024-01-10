#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for value in my_list:
        if value not in new_list:
            new_list.append(value)
    total = 0
    for _int in new_list:
        total += _int
    return total
