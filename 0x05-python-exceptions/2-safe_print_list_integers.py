#!/usr/bin/python3


def safe_print_list_integers(my_custom_list=[], custom_x=0):
    custom_count = 0
    for custom_i in range(custom_x):
        try:
            print("{:d}".format(my_custom_list[custom_i]), end="")
            custom_count += 1
        except (ValueError, TypeError):
            pass
    print()
    return custom_count
