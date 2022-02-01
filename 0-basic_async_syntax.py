#!/usr/bin/env python3
""" Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random """
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """ Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random """
    time = uniform(0, max_delay)
    await asyncio.sleep(time)
    return time