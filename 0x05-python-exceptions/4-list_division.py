#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            c_result = 0
            try:
                result.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                print("division by 0")
            except TypeError:
                print("wrong type")
            except IndexError:
                print("out of range")
            finally:
                result.append(c_result)
        except (TypeError, ValueError):
            print("wrong type")

    return result
