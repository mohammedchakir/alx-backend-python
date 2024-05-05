#!/usr/bin/env python3
"""
Measure Runtime Module
"""

import asyncio
import time
from typing import List
from async_comprehension import async_comprehension  # type: ignore


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing
    async_comprehension four times in parallel.
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.time()
    return end_time - start_time
