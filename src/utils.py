from typing import Callable, Iterable


def capitalize(func: Callable) -> Callable:
    def wrapper(*args) -> str:
        return func(*args).capitalize()

    return wrapper


def join(sep: str,
         iterable: Iterable) -> str:
    return f"{sep}{sep.join(iterable)}"


