#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul_dict = {key: value*2 for key, value in a_dictionary.items()}

    return mul_dict
