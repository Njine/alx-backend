#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents a simple cache system with no size limit.
    
    The BasicCache class allows storing and retrieving items
    from a dictionary.
    """
    
    def put(self, key: str, item: object):
        """Adds an item in the cache associated with the specified key.
        
        Args:
            key (str): The key for the cache item.
            item (object): The item to cache.
        
        If either the key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return
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
        return self.cache_data.get(key, None)
