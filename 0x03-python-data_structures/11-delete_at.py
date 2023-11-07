#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx > len(my_list) - 1 or idx < 0:
        return my_list
    else:
        new_list = [num for i, num in enumerate(my_list) if i != idx]
        return new_list
