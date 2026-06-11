#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list and returns a list of booleans.

    Args:
        my_list (list): The list containing integers to check.

    Returns:
        list: A new list with True or False at the corresponding positions.
    """
    result_list = []
    for num in my_list:
        if num % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list
