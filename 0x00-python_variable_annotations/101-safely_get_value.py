#!/usr/bin/env python3
"""
This script defines a function to safely retrieve
a value from a dictionary.
"""

from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.
    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to lookup in the dictionary.
        default (Optional[T]): The default value to return
        if the key is not found (default is None).
    Returns:
        Union[Any, T]: The value associated with the key
        if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == "__main__":
    annotations = safely_get_value.__annotations__

    print("Here's what the mappings should look like")
    for k, v in annotations.items():
        print("{}: {}".format(k, v))
