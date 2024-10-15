#!/usr/bin/env python3
"""2-measure_runtime.py"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay).

    Args:
    n(int): number of times wait_random is called in wait_n.
    max_delay(int): maximum delay for wait_n.

    Returns:
    (float): average time it takes for all tasks to run.
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    exec_time: float = end_time - start_time
    avg_time: float = exec_time / n
    return avg_time
