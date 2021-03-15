import re
from typing import Any, Callable, Generator

from marker import Alias, Inline, Multiline


Regex = str
MarkedText = str


inline_marks: dict[Regex, Callable] = {
    r"_date": Alias.abriged_date,
    r"_([\d]+)e": Alias.century,
    r"_([\d]+)": Alias.line_numbering,
    r"([^\n]+)[ \t]*::[ \t]*([^\n]+)": Inline.simple_definition
}

multiline_marks: dict[Regex, Callable] = {
    r"^\.\.[ \t]*([^\n]+)$": Multiline.conclusion,
    r"^&{1,6}[ \t]*([^\n]+)$": Multiline.title
}


def compiles(iterable: dict[Regex, Any]) -> Generator[Tuple[Regex, Any]]:
    return ((re.compile(regex), _)
                for regex, _ in iterable.items())


def parse_inline(text: MarkedText) -> Generator:
    for nb, line in enumerate(text.split("\n")):
        for regex, mark in compiles(inline_marks):
            pattern = regex.search(line)

            if pattern:
                args = pattern.groups()

                yield mark(*args)


STATEMENT = """
_date
_10e

"""

for i in parse_inline(STATEMENT):
    print(i)
