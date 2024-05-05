#!/usr/bin/env python3
"""Module to measure the runtime of wait_n coroutine."""

import time
from typing import List
from asyncio import run
from random import uniform
from asyncio import sleep

wait_n = __import__('1-concurrent_coroutines').wait_n


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds."""
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay), and returns total_time / n.
    Args:
        n: An integer specifying the number of times to execute wait_n.
        max_delay: An integer specifying the maximum delay for each execution of wait_n.
    Returns:
        A float representing the total execution time divided by n.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    total_time = time.time() - start_time
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(run(measure_time(n, max_delay)))
