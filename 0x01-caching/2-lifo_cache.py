#!/usr/bin/python3
"""
Last In First Out system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Last In First Out Caching algorithm
    """
    def __init__(self):
        """initialize"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add items to our dictionary
        also performs the Last In First out algorithm
        """
        if key and item:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict()
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """
        Retreive an item from the dict
        """
        return self.cache_data.get(key, None)

    def evict(self):
        """
        Pops the last key from the list and removes it
        from the cache
        """
        last = self.keys.pop()
        del self.cache_data[last]
        print('DISCARD: ', last)
