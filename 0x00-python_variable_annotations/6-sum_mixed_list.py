#!/usr/bin/env python3
"""
A type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and
floats and returns their sum as a float.
"""

from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """
    Returns sum of the list as a float
    """
    return float(sum(mxd_lst))
