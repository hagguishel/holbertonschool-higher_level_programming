#!/usr/bin/python3
"""
Prints text with 2 new lines after '.', '?' and ':'.
Removes leading spaces in each printed block.
"""


def text_indentation(text):
    """
    Print text with 2 new lines after '.', '?' and ':'.

    Args:
        text: The input text (string).

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")

        if text[i] in ".:?":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
