#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.

    Args:
        my_list (list): The initial list.
        search: The element to replace in the list.
        replace: The new element.

    Returns:
        list: A new list with the elements replaced.
    """
    return [replace if num == search else num for num in my_list]
