#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.

    Args:
        a_dictionary (dict): The dictionary containing name and score pairs.

    Returns:
        str: The key with the maximum value, or None if no score is found.
    """
    if not a_dictionary or len(a_dictionary) == 0:
        return None

    max_key = list(a_dictionary.keys())[0]
    max_val = a_dictionary[max_key]

    for key, value in a_dictionary.items():
        if value > max_val:
            max_val = value
            max_key = key

    return max_key
