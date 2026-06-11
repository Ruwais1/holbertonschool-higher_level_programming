#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Raises a NameError exception along with a specific custom message.

    Args:
        message (str): The custom message to embed in the NameError.
    """
    raise NameError(message)
