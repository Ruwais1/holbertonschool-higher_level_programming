#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Args:
        roman_string (str): The roman numeral string to convert.

    Returns:
        int: The converted integer value, or 0 if invalid input.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    length = len(roman_string)

    for i in range(length):
        current_val = roman_dict.get(roman_string[i], 0)
        if (i + 1 < length and
                roman_dict.get(roman_string[i + 1], 0) > current_val):
            total -= current_val
        else:
            total += current_val

    return total
