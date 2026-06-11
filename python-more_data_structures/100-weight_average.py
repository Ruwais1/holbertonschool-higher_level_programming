#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Returns the weighted average of all integers tuple (<score>, <weight>).

    Args:
        my_list (list): A list of tuples containing (score, weight).

    Returns:
        float: The weighted average, or 0 if the list is empty.
    """
    if not my_list or len(my_list) == 0:
        return 0

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    return total_score / total_weight
