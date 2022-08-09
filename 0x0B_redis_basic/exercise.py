#!/usr/bin/env python3
"""
Redis basic module
"""
from typing import Union, Callable, Optional
import redis
import uuid
import sys
from functools import wraps


def count_calls(f: Callable) -> Callable:
    """
    Create and return function that increments the count
    for that key every time the method is called and returns
    the value returned by the original method.
    """
    key = f.__qualname__

    @wraps(f)
    def wrapper(self, *args, **kwds):
        """
        wrapper function
        """
        self._redis.incr(key)
        return f(self, *args, **kwds)
    return wrapper


class Cache:
    """ Cache class
    """

    def __init__(self):
        """ __init __
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Takes a data argument and returns a string. The method
        should generate a random key (e.g. using uuid), store the input
        data in Redis using the random key and return the key.
        """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """  Reading from Redis and recovering original type
        """
        res = self._redis.get(key)
        return fn(res) if fn else res

    def get_str(self, data: bytes) -> str:
        """
        Converts bytes to string.
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """
        Converts bytes to int.
        """
        return int.from_bytes(data, sys.byteorder)