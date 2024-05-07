#!/usr/bin/env python3
"""Async Generator Module"""
import asyncio
import random
from typing import AsyncGenerator, Any


async def async_generator() -> AsyncGenerator[Any, Any]:
    """Loop 10 times, wait 1 sec each time"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
