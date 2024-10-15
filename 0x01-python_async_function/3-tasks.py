#!/usr/bin/env python3
"""3-tasks"""
import asyncio
wait_random = __import__('1-concurrent_coroutines').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task[float]:
    """Creates a task from an existing coroutine.
    Args:
        max_delay(int): the maximum delay time.
    Returns:
    asyncio.Task[float]: the task created
    """
    task: asyncio.Task[float] = asyncio.create_task(wait_random(max_delay))
    return task
