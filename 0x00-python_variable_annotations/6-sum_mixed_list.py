#!/usr/bin/env python3
"""takes a list mxd_lst of integers and floats"""
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """returns their sum as a float"""
    return float(sum(mxd_list))
