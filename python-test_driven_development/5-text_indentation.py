#!/usr/bin/python3
"""
This module provides a function that indents text based on punctuation.
It handles strict string verification and eliminates inner padding spaces.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    Ensures no spaces exist at the beginning or end of any printed line.

    Args:
        text (str): The text string to parse and print.

    Raises:
        TypeError: If text is not a primitive string type.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    length = len(text)
    i = 0

    while i < length:
        print(text[i], end="")

        if text[i] in ('.', '?', ':'):
            print("\n")

            while i + 1 < length and text[i + 1] == ' ':
                i += 1

        i += 1
