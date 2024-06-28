#!/usr/bin/env python3
"""
Simple helper Function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a tuple with the start and end index
    from the parameters given
    """
    step: int = page_size
    for i in range(page):
        startIdx = i * step
        endIdx = step * (i + 1)

    return ((startIdx, endIdx))
