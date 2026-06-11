#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().

    Args:
        value: The value to be printed, can be of any type.

    Returns:
        bool: True if value was correctly printed as an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
