#!/usr/bin/env python3
"""
Async Comprehension Module
"""

import asyncio
from typing import List
from random import uniform
from async_generator import async_generator  # type: ignore


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers asynchronously.
    """
    return [num async for num in async_generator()]
