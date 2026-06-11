#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.

    Args:
        my_list (list): The list containing elements of any type.
        x (int): The number of elements to access in my_list.

    Returns:
        int: The real number of integers printed.
    """
    count = 0
    for i in range(x):
        value = my_list[i]
        try:
            print("{:d}".format(value), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print("")
    return count
