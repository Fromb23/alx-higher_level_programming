#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_copy = my_list[:]
    for element in range(len(list_copy)):
        if search == list_copy[element]:
            list_copy[element] = replace
    return list_copy
