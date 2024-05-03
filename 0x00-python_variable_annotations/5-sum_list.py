#!/usr/bin/env python3
"""
Module to calculate the sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function to calculate the sum of a list of floats.
    Args:
        input_list (List[float]): The list of floats.
    Returns:
        float: The sum of the floats in the list.
    """
    return sum(input_list)


if __name__ == "__main__":
    floats = [3.14, 1.11, 2.22]
    floats_sum = sum_list(floats)
    print(floats_sum == sum(floats))
    print(sum_list.__annotations__)
    print("sum_list(floats) returns {} which is a {}".format(floats_sum,
                                                             type(floats_sum)))
