#!/usr/bin/python3
"""
First In First Out implementation
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Caching. Will discard the first item
    if dict len is > the max length
    """

    def put(self, key, item):
        """
        First item is removed every time the dict
        exceeds limit
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            for idx, i in enumerate(self.cache_data):
                if idx == 0:
                    del self.cache_data[i]
                    print("DISCARD:", i)
                break

    def get(self, key):
        """
        Retreive the value from the dict
        using the key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        val = self.cache_data[key]
        return val
