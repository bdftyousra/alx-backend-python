#!/usr/bin/env python3
"""
This is a module that provides a function for summing list values.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function adds two numbers and returns the result.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The sum of a and b.
    """
    return sum(input_list)
