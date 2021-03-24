"""This module contains functions that are useful for the other modules.
"""

from typing import Any, Callable, Iterable, Generator

from .data import Config


def capitalize(func: Callable) -> Callable:
    """Returns the text given with the first letter capitalized if
    Config.capitalize is true.
    """
    def wrapper(*args: Any):
        if Config.capitalize:
            return func(*args).capitalize()
        else:
            return func(*args)

    return wrapper


def join(sep: str,
         iterable: Iterable) -> str:
    """Same behavior as str.join but the first element of the given iterable
    is prefixed with the given separator.
    """
    return "{sep}{sep.join(iterable)}"


def to_roman(nb: int) -> str:
    """Returns the given number as string in roman numerals."""
    romans = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    def roman_nb(nb: int) -> Generator[str, None, None]:
        for roman in romans.keys():
            x = nb//roman

            yield romans[roman]*x

            nb -= roman*x

            if nb <= 0:
                break

    return "".join(roman_nb(nb))
