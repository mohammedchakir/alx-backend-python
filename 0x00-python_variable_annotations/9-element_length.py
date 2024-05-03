#!/usr/bin/env python3

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function to return a list of tuples containing each element
    from the input list and its corresponding length.
    Args:
        lst (Iterable[Sequence]): The input list of sequences.
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing
        each element from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]


if __name__ == "__main__":
    print(element_length.__annotations__)
