#!/usr/bin/env python3
"""
This module provides functions for performing various
asynchronous operations.
"""
import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int) -> float:
    """
    Asynchronously waits for a random amount of time
    between 0 and max_delay.
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
        max_delay: The maximum delay in seconds for each call
        to wait_random.
    Returns:
        A list of all the delays (float values) in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    completed_delays = await asyncio.gather(*delays)
    return sorted(completed_delays)


if __name__ == "__main__":
    import asyncio

    async def test_wait_n():
        print(await wait_n(5, 5))
        print(await wait_n(10, 7))
        print(await wait_n(10, 0))

    asyncio.run(test_wait_n())
