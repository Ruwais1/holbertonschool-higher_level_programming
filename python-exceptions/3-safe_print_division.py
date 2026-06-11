#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides 2 integers and prints the result inside a finally block.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float: The result of the division, or None if ZeroDivisionError occurs.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
    return result
