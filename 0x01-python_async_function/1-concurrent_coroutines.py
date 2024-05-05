#!/usr/bin/env python3
"""Asynchronous coroutine that spawns wait_random n times
with the specified max_delay."""

import asyncio
from typing import List
from random import uniform

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that spawns wait_random n times
    with the specified max_delay."""
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)


if __name__ == "__main__":
    import asyncio
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
