#!/usr/bin/env python3
"""Module to create asyncio.Tasks for wait_n coroutine."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that spawns wait_random n times
    with the specified max_delay."""
    delays = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that creates an asyncio.Task for
    wait_n coroutine."""
    return await wait_n(n, max_delay)


if __name__ == "__main__":
    import asyncio

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
