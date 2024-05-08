#!/usr/bin/env python3
"""First-In First-Out caching module."""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system with a limited size.

    This class implements a FIFO cache that stores items in an
    OrderedDict. When the limit is exceeded, it discards the
    oldest item.
    """

    def __init__(self):
        """Initializes the cache with an empty OrderedDict."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key: str, item: object):
        """Adds an item to the cache.

        Args:
            key (str): The key for the cache item.
            item (object): The item to cache.

        If either the key or item is None, this method does nothing.
        If the number of items in the cache exceeds `MAX_ITEMS`,
        the oldest item (first-in) is discarded, following FIFO rules.
        """
        if key is None or item is None:
            return
        
        self.cache_data[key] = item

        # If the cache exceeds MAX_ITEMS, discard the first item (FIFO)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))  # Get the first key
            self.cache_data.pop(first_key)  # Remove the first item
            print("DISCARD:", first_key)

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
