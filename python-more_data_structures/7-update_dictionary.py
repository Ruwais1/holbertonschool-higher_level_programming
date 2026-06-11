#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds a key/value pair in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to check or create.
        value: The value to assign to the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
