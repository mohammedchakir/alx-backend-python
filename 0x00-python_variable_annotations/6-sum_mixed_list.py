#!/usr/bin/env python3
"""
Module to calculate the sum of a list of mixed integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function to calculate the sum of a list of mixed integers and floats.
    Args:
        mxd_lst(List[Union[int,float]]): The list of mixed integers and floats.
    Returns:
        float: The sum of the integers and floats in the list.
    """
    return sum(mxd_lst)


if __name__ == "__main__":
    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)
    print(sum_mixed_list.__annotations__)
    print(ans == sum(mixed))
    print("sum_mixed_list(mixed) returns {} which is a {}".format(ans,
                                                                  type(ans)))
