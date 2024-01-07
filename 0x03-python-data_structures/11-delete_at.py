#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        my_list[:] = [my_list[i] for i in range(len(my_list)) if i != idx]
    return my_list
