#!/usr/bin/env python3
"""Hypermedia pagination sample.
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: The start and end index for the given page and size.
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
        """Returns the cached dataset.

        If the dataset hasn't been loaded yet, it reads the data from the CSV
        file and removes the header.

        Returns:
            List[List]: The dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data from the dataset.

        Args:
            page (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            List[List]: The dataset for the given page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns pagination information and data for a given page.

        Args:
            page (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing pagination information and data.
        """
        # Get the data for the current page
        page_data = self.get_page(page, page_size)

        # Calculate the total number of pages
        total_pages = math.ceil(len(self.dataset()) / page_size)

        # Determine the next page number, or None if there's no next page
        next_page = page + 1 if (page - 1) * page_size + page_size < len(self.dataset()) else None

        # Determine the previous page number, or None if no previous page
        prev_page = page - 1 if page > 1 else None

        # Create a dictionary with pagination information and data
        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }
