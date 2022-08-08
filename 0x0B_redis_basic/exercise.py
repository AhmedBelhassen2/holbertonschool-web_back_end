#!/usr/bin/env python3
""" The open source, in-memory data store used by millions of developers as a database, cache, streaming engine, and message broker. """
from typing import Union, Callable, Optional, Any
import redis
import uuid

class Cache:
    """ class """
    def __init__(self):
        """ Create a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ method that takes a data argument and returns a string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
