#!/usr/bin/python3

""" The basics of async """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ The basic caching """

    def put(self, key, item):
        """ Put a key/value pair """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get a key/value pair """
        return self.cache_data.get(key, None)
