#!/usr/bin/env python3
'''6-sum_mixed_list'''
from typing import TypeAlias
Vector: TypeAlias = list[float, int]


def sum_mixed_list(mxd_list: Vector) -> float:
    '''
    Adds the elements  of a list.

    Args:
        mxd_list(Vector): the list of floats.

    Returns:
        sum(float): the sum of the elements.
    '''
    sum = 0
    for num in mxd_list:
        sum += num
    return sum
