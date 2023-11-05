#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for idx, elemnt in enumerate(x):
            print("{:d}".format(elemnt), end=" " if idx < len(x) - 1 else "")
        print()
