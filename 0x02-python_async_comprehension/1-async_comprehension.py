#!/usr/bin/env python3
"""Async Comprehension Module"""

import asyncio
from typing import List
from importlib import import_module

async_generator_module = import_module("0-async_generator")
async_generator = async_generator_module.async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using
    async comprehension over async_generator.
    """
    return [i async for i in async_generator()]
