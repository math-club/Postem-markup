from typing import Callable, Iterable

from data import Config


def capitalize(func: Callable) -> Callable:
    def wrapper(*args) -> str:
        if Config.capitalize:
            return func(*args).capitalize()
        else:
            return func(*args)

    return wrapper


def join(sep: str,
         iterable: Iterable) -> str:
    return f"{sep}{sep.join(iterable)}"


def to_roman(nb: int) -> str:
    roman = {
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

    def roman_nb(nb):
        for r in roman.keys():
            x, y = divmod(nb, r)

            yield roman[r]*x

            nb -= r*x

            if nb <= 0:
                break

    return "".join(i for i in roman_nb(nb))
