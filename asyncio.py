# asyncio: Asynchronous I/O, event loop, coroutines and tasks
# https://docs.python.org/3/library/asyncio.html
# asyncio provides infrastructure for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources,
# running network clients and servers, and other related primitives

# The asyncio module provides a framework that revolves around the event loop. The event loop is the core of every asyncio application.
# Event loops run asynchronous tasks and callbacks, perform network IO operations, and run subprocesses.
# asyncio provides a coroutine-based API that is designed to be similar to the threading module.
# A coroutineis a special function that can give up control to its caller without losing its state
# The async and await keywords were added in Python 3.5 to define a native coroutine and make them a distinct type when compared with a generator based coroutine

import asyncio


async def my_coro():
    await func()
