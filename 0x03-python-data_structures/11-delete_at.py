#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < len(my_list) - 1:
        return my_list
    else:
        return my_list.remove(my_list[idx])