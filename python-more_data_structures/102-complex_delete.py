#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to modify.
        value: The target value whose associated keys should be deleted.

    Returns:
        dict: The updated dictionary.
    """
    if not isinstance(a_dictionary, dict) or a_dictionary is None:
        return a_dictionary

    keys_to_delete = [k for k, v in a_dictionary.items() if v == value]

    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
