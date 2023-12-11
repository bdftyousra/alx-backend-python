#!/usr/bin/env python3
"""
A module for creating asyncio Tasks that run asynchronous functions.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task that waits for a random amount of time
    up to `max_delay` seconds when run.
    Returns the created Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
