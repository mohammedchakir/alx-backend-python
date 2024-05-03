#!/usr/bin/env python3
"""
This script defines a function to safely retrieve
the first element of a sequence.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Function to safely retrieve the first element of a sequence.
    Args:
        lst (Sequence): The input sequence.
    Returns:
        Union[Any, None]: The first element of the sequence
        if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None


if __name__ == "__main__":
    print(safe_first_element.__annotations__)
