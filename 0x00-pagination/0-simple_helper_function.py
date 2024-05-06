#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple representing the start and end index for pagination.

    Args:
        page (int): The page number, starting from 1.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple with the start and end index for the items
        on the given page.
    """
    # Calculate the start index by multiplying (page - 1) with page_size
    start = (page - 1) * page_size
    # Calculate the end index by adding the page_size to start
    end = start + page_size
    # Return a tuple with the calculated start and end indices
    return (start, end)
