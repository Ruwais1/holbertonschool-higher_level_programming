#!/usr/bin/python3
"""
5-text_indentation module.

This module provides a function `text_indentation` that formats text
by splitting lines after specific punctuation characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = True
    for char in text:
        if skip_space and char == " ":
            continue

        skip_space = False
        print(char, end="")

        if char in (".", "?", ":"):
            print("\n")
            skip_space = True
