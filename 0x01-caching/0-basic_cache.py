#!/usr/bin/python3
"""
Basic Dictionary implementation
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Implementing a dictionary system
    """

    def put(self, key, item):
        """
        Assigns the dictionary self.cache_data item to the key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retreive values from the dictionary
        """
        if key is None or key not in self.cache_data.keys():
            return None
        val = self.cache_data[key]
        return val
