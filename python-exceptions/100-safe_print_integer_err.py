#!/usr/bin/python3
def safe_print_integer_err(value):
    """
    Prints an integer using "{:d}".format() and logs errors to stderr.

    Args:
        value: The value to print, can be of any data type.

    Returns:
        bool: True if the value printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        import sys
        sys.stderr.write("Exception: {}\n".format(e))
        return False
