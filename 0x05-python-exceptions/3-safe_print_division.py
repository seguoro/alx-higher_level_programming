#!/usr/bin/python3


def safe_print_division(a, b):
    result = None  # Initialize result outside the try block
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    except Exception as e:
        print("Exception:", e)
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        print("Finally: Inside result: {}".format(result))
