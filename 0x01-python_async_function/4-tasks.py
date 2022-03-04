#!/usr/bin/env python3
'''Let's execute multiple coroutines at the same time with async'''


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''spawn wait_random n times with the specified max_delay'''
    queue, array = [], []
    for i in range(n):
        queue.append(wait_random(max_delay))
    for j in asyncio.as_completed(queue):
        result = await j
        array.append(result)
    return sorted(array)
