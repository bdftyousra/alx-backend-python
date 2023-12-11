#!/usr/bin/env python3
"""
This is a module that provides a function for summing list values.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function computes the sum of a list of integers and floats, and
        returns the result as a float.

    Parameters:
    mxd_lst (List[Union[int, float]]): The list of integers and floats to sum.

    Returns:
    float: The sum of the elements in mxd_lst.
    """
    return sum(mxd_lst)
