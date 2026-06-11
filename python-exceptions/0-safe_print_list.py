#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list safely using try/except blocks.

    Args:
        my_list (list): The list containing elements of any type.
        x (int): The number of elements to print.

    Returns:
        int: The real number of elements successfully printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
