#!/usr/bin/env python3
"""Least Frequently Used caching module."""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU caching system with a limited size.

    This class implements an LFU cache that uses an OrderedDict
    for storage. When the cache exceeds the limit, the least
    frequently used item is removed. If there are multiple such
    items, the least recently used one is removed.
    """

    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = OrderedDict()  # Keeps track of the access frequency

    def __update_frequency(self, key):
        """Updates the frequency of a given key."""
        self.keys_freq[key] = self.keys_freq.get(key, 0) + 1
        self.cache_data.move_to_end(key, last=False)

    def put(self, key: str, item: object):
        """Adds an item in the cache.

        Args:
            key (str): The key for the cache item.
            item (object): The item to cache.

        If the key or item is None, this method does nothing.
        If the cache limit is reached, the least frequently used
        item is removed. If there's a tie, the least recently used
        among them is discarded.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key(s)
                min_freq = min(self.keys_freq.values())
                lfu_keys = [k for k, v in self.keys_freq.items() if v == min_freq]
                lfu_key = lfu_keys[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop(lfu_key)
                print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.keys_freq[key] = 1
        else:
            # If the key is already in the cache, update its frequency
            self.cache_data[key] = item
            self.__update_frequency(key)

    def get(self, key: str) -> object:
        """Retrieves an item from the cache by its key.

        Args:
            key (str): The key for the cache item.

        Returns:
            object: The cached item, or None if the key doesn't exist
            or if the key is None.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency for the key when accessed
        self.__update_frequency(key)
        return self.cache_data.get(key)
