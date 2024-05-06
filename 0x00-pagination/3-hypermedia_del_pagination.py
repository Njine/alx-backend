#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude the header row

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieves dictionary with pagination information based on index.

        Args:
            index (int): The start index for the page.
            page_size (int): The number of items per page.

        Returns:
            Dict: Pagination information with current index, page data,
            next index, and page size.
        """
        assert index is not None and index >= 0 and index < len(self.indexed_dataset())

        # List to store page data
        page_data = []
        # Flag to track the next index
        next_index = None

        # Find the page data starting from the given index
        start = index
        for i in range(start, len(self.indexed_dataset())):
            if len(page_data) < page_size:
                page_data.append(self.indexed_dataset()[i])
            else:
                next_index = i
                break

        # If reached end & haven't filled page, next_index remains None
        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }
