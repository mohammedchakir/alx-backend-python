#!/usr/bin/env python3
"""
Module to concatenate two strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Function to concatenate two strings.
    Args:
        str1 (str): The first string.
        str2 (str): The second string.
    Returns:
        str: The concatenated string.
    """
    return str1 + str2


if __name__ == "__main__":
    str1 = "egg"
    str2 = "shell"
    concat(str1, str2)
