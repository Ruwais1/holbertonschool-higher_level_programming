#!/usr/bin/python3
def magic_calculation(a, b):
    """
    Reconstructs Python bytecode logic involving a loop, custom exception
    handling, mathematical operations, and loop breaking mechanisms.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / i
        except Exception:
            result = b + a
            break
    return result
