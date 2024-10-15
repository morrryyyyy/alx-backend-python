#!/usr/bin/env python3
"""4-tasks.py"""
import asyncio
from typing import List
# Import wait_random from the previously defined module
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of all the delay times in seconds.
    """
    tasks: List[asyncio.Task] = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    results: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)
    return results
