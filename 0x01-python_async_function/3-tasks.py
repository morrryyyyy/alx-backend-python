#!/usr/bin/env python3
"""3-tasks"""
import asyncio
from typing import Any
wait_random = __import__('1-concurrent_coroutines').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task[Any]:
    """Creates a task from an existing coroutine.
    Args:
        max_delay(int): the maximum delay time.
    Returns:
    asyncio.Task[Any]: the task created
    """
    task: asyncio.Task[Any] = asyncio.create_task(wait_random(max_delay))
    return task
