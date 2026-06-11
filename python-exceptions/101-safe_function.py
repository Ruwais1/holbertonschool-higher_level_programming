#!/usr/bin/python3
def safe_function(fct, *args):
    """
    Executes a function safely and logs any runtime exceptions to stderr.

    Args:
        fct: A pointer to the function to execute.
        *args: Variable length argument list for the function fct.

    Returns:
        The result of the function execution, or None if an exception occurs.
    """
    try:
        return fct(*args)
    except Exception as e:
        import sys
        sys.stderr.write("Exception: {}\n".format(e))
        return None
