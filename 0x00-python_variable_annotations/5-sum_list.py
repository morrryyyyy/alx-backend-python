#!/usr/bin/env python3
'''5-sum_list.py'''
from typing import TypeAlias
Vector: TypeAlias = list[float]


def sum_list(input_list: Vector) -> float:
    '''
    Adds the elements  of a list.

    Args:
        input_list(Vector): the list of floats.

    Returns:
        sum(float): the sum of the elements.
    '''
    sum = 0
    for num in input_list:
        sum += num
    return sum
