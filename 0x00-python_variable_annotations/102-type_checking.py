#!/usr/bin/env python3
"""
Zooms in on each element of the input tuple by repeating
each element by a specified factor.
"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """
    Zooms in on each element of the input tuple by repeating
    each element by a specified factor.
    Args:
        lst (Tuple[Any, ...]): The input tuple.
        factor (int): The factor by which each element
        should be repeated (default is 2).
    Returns:
        Tuple[Any, ...]: The zoomed-in tuple.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)


if __name__ == "__main__":
    array = (12, 72, 91)

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3)

    print(zoom_2x)
    print(zoom_3x)
