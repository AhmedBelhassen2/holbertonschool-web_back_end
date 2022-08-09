#!/usr/bin/env python3
""" The open source, in-memory data store used by millions of developers as a database, cache, streaming engine, and message broker. """
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
    """ class """
    def __init__(self):
        """ Create a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb. """
        self._redis = redis.Redis()
        self._redis.flushdb()
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ method that takes a data argument and returns a string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """  This callable will be used to convert the data back to the desired format. """
        rds = self._redis.get(key)
        return fn(rds) if fn else rds

    def get_str(self, data: bytes) -> str:
        """ Converts bytes to string. """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Converts bytes to int. """
        return int.from_bytes(data, sys.byteorder)

    