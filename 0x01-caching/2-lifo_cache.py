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

    def put(self, key, item):
        """
        LIFO - if the limit is exceeded, then delete the last item
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            list_of_last_items = list(self.cache_data.keys())
            last_in_item = list_of_last_items[-2]
            self.cache_data.pop(last_in_item)
            print('DISCARD: ', last_in_item)

    def get(self, key):
        """
        Retreive data from the dict using the key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        val = self.cache_data[key]
        return val
