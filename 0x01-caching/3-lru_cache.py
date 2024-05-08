#!/usr/bin/env python3
"""Least Recently Used caching module."""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system with a limited size.

    This class implements an LRU cache that stores items in an
    OrderedDict. When the cache limit is reached, it discards
    the least recently used item.
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
        If the cache exceeds `MAX_ITEMS`, it removes the least
        recently used item and prints "DISCARD:" with the discarded key.
        """
        if key is None or item is None:
            return

        # If the cache already contains the key, update it
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        else:
            # If the cache limit is reached, discard the least recently used item (LRU)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD:", lru_key)
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

        # If the key exists, mark it as recently used
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        
        return self.cache_data.get(key)
