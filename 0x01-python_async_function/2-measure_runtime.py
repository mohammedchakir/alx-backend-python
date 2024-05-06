#!/usr/bin/env python3
"""
This module provides functions for measuring the runtime
of asynchronous operations.
"""
import asyncio
import time
from typing import List
from random import uniform


async def wait_random(max_delay: int) -> float:
    """
    Asynchronously waits for a random amount of time between
    0 and max_delay.
    Args:
        max_delay: The maximum delay in seconds.
    Returns:
        The actual delay in seconds.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns wait_random n times with the
    specified max_delay.
    Args:
        n: The number of times to spawn wait_random.
        max_delay: The maximum delay in seconds for each
        call to wait_random.
    Returns:
        A list of all the delays (float values) in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    completed_delays = await asyncio.gather(*delays)
    return sorted(completed_delays)


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay),
    and return total_time / n.
    Args:
        n: The number of times to call wait_random.
        max_delay: The maximum delay in seconds for each call
        to wait_random.
    Returns:
        The average time taken for each call to wait_random.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
