#!/usr/bin/env python3
"""Most Recently Used caching module."""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system with a limited size.

    This class implements an MRU cache that stores items in an
    OrderedDict. When the cache limit is reached, it discards
    the most recently used item.
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

        If the key or item is None, this method does nothing.
        If the cache limit is reached, it removes the most recently
        used item and prints "DISCARD:" with the discarded key.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the most recently used item (MRU)
            mru_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD:", mru_key)
        
        # Add the new item and mark it as most recently used
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

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
        
        # If the key exists, mark it as most recently used
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)

        return self.cache_data.get(key)
