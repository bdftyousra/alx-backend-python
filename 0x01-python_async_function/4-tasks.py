#!/usr/bin/env python3
"""
A module for creating and running multiple asyncio Tasks concurrently.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create and run `n` asyncio Tasks that wait for random amounts of time
    up to `max_delay` seconds. Returns a list of the Task objects, sorted
    in ascending order by the time waited.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
