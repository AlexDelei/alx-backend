#!/usr/bin/python3
"""
Last In First Out system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Last In First Out Caching algorithm
    """
    def put(self, key, item):
        """
        LIFO - if the limit is exceeded, then delete the last item
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            for idx, i in enumerate(reversed(self.cache_data)):
                if idx == 0:
                    del self.cache_data[i]
                    print("DISCARD:", i)
                break

    def get(self, key):
        """
        Retreive data from the dict using the key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        val = self.cache_data[key]
        return val
