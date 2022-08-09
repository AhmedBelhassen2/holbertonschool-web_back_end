#!/usr/bin/env python3
""" The open source, in-memory data store used
by millions of developers as a database, cache,
streaming engine, and message broker. """
from typing import Union, Callable, Optional
import redis
import uuid
import sys
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Create and return function that increments the count
    for that key every time the method is called and returns
    the value returned by the original method.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        wrapper function
        """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs
    for a particular function.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        """
        wrapper function
        """
        self._redis.rpush("{}:inputs".format(key), str(args))
        result = method(self, *args)
        self._redis.rpush("{}:outputs".format(key),
                          str(result))
        return result
    return wrapper


class Cache:

    """ class """

    def __init__(self):
        """ Create a Cache class. In the __init__ method,
        store an instance of the Redis client as a private
        variable named _redis (using redis.Redis())
        and flush the instance using flushdb. """
        self._redis = redis.Redis()
        self._redis.flushdb()
    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ method that takes a data argument and returns a string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn:
            Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """  This callable will be used to convert
        the data back to the desired format. """
        rds = self._redis.get(key)
        return fn(rds) if fn else rds

    def get_str(self, data: bytes) -> str:
        """ Converts bytes to string. """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Converts bytes to int. """
        return int.from_bytes(data, sys.byteorder)
