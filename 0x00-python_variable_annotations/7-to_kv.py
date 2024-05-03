#!/usr/bin/env python3
"""
Module to convert a string and an int or float to a tuple
with the string and the square of the int or float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function to convert a string and an int or float to a
    tuple with the string and the square of the int or float.
    Args:
        k (str): The string key.
        v (Union[int, float]): The int or float value.
    Returns:
        Tuple[str, float]: A tuple with the string key and
        the square of the int or float value.
    """
    return (k, v * v)


if __name__ == "__main__":
    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
