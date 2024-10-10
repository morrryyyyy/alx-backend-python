#!/usr/bin/env python3
'''8-make_multiplier'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''make multiplier function'''
    def multiply(value: float) -> float:
        return value * multiplier
    return multiply
