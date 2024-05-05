#!/usr/bin/env python3
"""Module to create asyncio.Tasks."""

import asyncio
from asyncio import Task
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Create an asyncio.Task for wait_random coroutine with
    the specified max_delay.
    Args:
        max_delay: An integer specifying the maximum dela
        for wait_random.
    Returns:
        An asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    import asyncio

    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
