#!/usr/bin/env python3
"""Simple pagination sample.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the start and end index for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple with the start and end index for the items
        to retrieve from the dataset.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset.

        Returns:
            List[List]: The dataset after removing the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Remove the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of the dataset based on given page number and size.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list representing the data for the specified page.
        """
        # Ensure page and page_size are integers greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Get the start and end index for the requested page
        start, end = index_range(page, page_size)

        # Retrieve the dataset and return the relevant slice
        data = self.dataset()
        if start >= len(data):
            return []

        return data[start:end]
