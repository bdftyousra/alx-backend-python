#!/usr/bin/env python3
"""
This is a module that provides a function for finding the length of each
    element in a list of strings.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes a list of strings and returns a list of tuples,
        where each tuple contains a string and the length of that string.

    Parameters:
    lst (List[str]): The list of strings to process.

    Returns:
    List[Tuple[str, int]]: A list of tuples, where each tuple contains
        a string and the length of that string.
    """
    return [(i, len(i)) for i in lst]
