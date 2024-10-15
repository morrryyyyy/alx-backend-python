#!/usr/bin/env python3
"""0-basic_async_syntax.py"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that waits for a random delay between 0 and max_delay seconds
    and returns the delay.

    Args:
        max_delay (int): the maximum waiting time (default is 10 seconds).

    Returns:
        float: The actual delay time in seconds.
    """
    delay: float = random.uniform(0, max_delay)  # Get a random float between 0 and max_delay
    await asyncio.sleep(delay)  # Asynchronously wait for the delay time
    return delay
