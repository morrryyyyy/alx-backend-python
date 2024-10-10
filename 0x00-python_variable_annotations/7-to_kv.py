#!/usr/bin/env python3
'''7-to_kv'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Args:
    k(str): a stirng
    v(Union[int, float]): the second argument

    RETURNS:
    Tuple
    '''
    return (k, float(v ** 2))
