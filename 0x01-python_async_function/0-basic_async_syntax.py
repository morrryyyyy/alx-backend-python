#!/usr/bin/env python3
"""0-basic_async_syntax.py"""
import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """
    A coroutine that waits for a while, and returns the amount of time delayed.

    Args:
        max_delay(int): the maximum waiting time

    Returns:
    delay(float): the actual waiting time.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
