#!/usr/bin/env python3
"""Last-In First-Out caching module."""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system with a limited size.

    This class implements a LIFO cache that stores items in an
    OrderedDict. When the limit is exceeded, it discards the
    most recently added item.
    """

    def __init__(self):
        """Initializes the cache with an empty OrderedDict."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key: str, item: object):
        """Adds an item in the cache.

        Args:
            key (str): The key for the cache item.
            item (object): The item to cache.

        If the key or item is None, this method does nothing.
        If the number of items in the cache exceeds `MAX_ITEMS`,
        the most recently added item (LIFO) is discarded.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the most recently added item (LIFO)
            last_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD:", last_key)

        self.cache_data[key] = item

    def get(self, key: str) -> object:
        """Retrieves an item from the cache by its key.

        Args:
            key (str): The key for the cache item.

        Returns:
            object: The cached item, or None if the key doesn't exist
            or if the key is None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
