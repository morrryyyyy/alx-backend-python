#!/usr/bin/env python3
"""3-tasks"""
from asyncio import Task, create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Creates a task from an existing coroutine.

    Args:
        max_delay (int): The maximum delay time.

    Returns:
        asyncio.Task[float]: The task created.
    """
    # Create a task using the wait_random coroutine
    task: Task = create_task(wait_random(max_delay))
    return task
