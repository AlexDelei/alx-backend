#!/usr/bin/python3
"""
MRU - Most Recently Used cache algorithm
"""
from collections import OrderedDict, deque
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Discarding the most recently used item (MRU algorithm)
    """
    def __init__(self):
        """
        Initialize first
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.queue = deque()

    def put(self, key, item):
        """
        Add an item to the cache. If the cache exceeds the limit,
        discard the most recently used item.
        """
        if key is None or item is None:
            return

        # Update the key-value item
        if key in self.cache_data:
            del self.cache_data[key]

        # Removing the last item inserted
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.evict()

        self.cache_data[key] = item

    def get(self, key):
        """
        Retreive an item from the cache
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

    def evict(self):
        """
        Pop out the last item in the dictionary
        """
        last, _ = self.cache_data.popitem(last=True)
        print(f'DISCARD: {last}')
