"""This module contains decorators to provide additional parsing to the
arguments of the functions contained in the marker module.
"""

from typing import Any, Callable


def parse_title(func: Callable) -> Callable:
    """A decorator to determine the level of a title."""
    def wrapper(title_level: str, text: str):
        return func(text, len(title_level))

    return wrapper
