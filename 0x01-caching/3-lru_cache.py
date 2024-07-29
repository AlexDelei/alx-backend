#!/usr/bin/python3
"""
discard the least recently used item (LRU algorithm)
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    discard the least recently used item (LRU algorithm)
    """
    def __init__(self):
        """initialize"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        LRU - discards the recently used item
        """
        if key is None or item is None:
            return

        # Replacing old entry with a new position later
        if key in self.cache_data:
            del self.cache_data[key]

        self.cache_data[key] = item

        # Poping the first item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = self.cache_data.popitem(last=False)
            print("DISCARD: ", last[0])

    def get(self, key):
        """
        retreives value aligning with the key provided
        """
        if key is None or key not in self.cache_data.keys():
            return None

        # Moving accessed item to the end to mark it as
        # recently used
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
