#!/usr/bin/env python3
"""
Module to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function to create a multiplier function.
    Args:
        multiplier (float): The multiplier value.
    Returns:
        Callable[[float], float]: A function that multiplies a float
        by the given multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function


if __name__ == "__main__":
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
