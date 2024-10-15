#!/usr/bin/env python3
"""
An asynchronus coroutine that takes an integer argument
'max_delay' named wait_random that waits for random delay
between 0 and max_delay seconds and eventually returns it
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async function"""
    value = random.random() * max_delay
    await asyncio.sleep(value)
    return value
