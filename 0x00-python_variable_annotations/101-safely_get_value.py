#!/usr/bin/env python3
"""
This is a module that provides a function for safely getting a value from
    a mapping.
"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    This function gets the value for a given key in a mapping, or returns
        a default value if the key is not in the mapping.

    Parameters:
    dct (Mapping): The mapping to get the value from.
    key (Any): The key to look up in the mapping.
    default (Union[T, None]): The default value to return if the key is not
        in the mapping.

    Returns:
    Union[Any, T]: The value for the key in the mapping, or the default
        value if the key is not in the mapping.
    """
    if key in dct:
        return dct[key]
    else:
        return default
