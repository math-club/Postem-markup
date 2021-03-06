"""This module contains the filtering patterns for each tag and the
functions useful for compilation.
"""

import re
from typing import Any, Callable, Dict, Generator, Tuple

from marker import Alias, Inline, Multiline


Regex = str
MarkedText = str

inline_marks: Dict[Regex, Callable] = {
    r"_date": Alias.abriged_date,
    r"_([\d]+)e": Alias.century,
    r"_([\d]+)": Alias.line_numbering,
    r"([^\n]+)[ \t]*::[ \t]*([^\n]+)": Inline.simple_definition
}

multiline_marks: Dict[Regex, Callable] = {
    r"^\.\.[ \t]*([^\n]+)$": Multiline.conclusion,
    r"^(&{1,6})[ \t]*([^\n]+)$": Multiline.title
}


def compiles(iterable: Dict[Regex, Any]) -> Dict[re.Pattern, Any]:
    """Returns the given dictionary with these compiled keys."""
    return {re.compile(key): value
                for key, value in iterable.items()}


def parse_inline(text: MarkedText) -> Generator[str, None, None]:
    patterns = compiles(inline_marks)
    for line in text.split("\n"):
        for pattern, mark in patterns.items():
            for matchobj in pattern.finditer(line):
                args = matchobj.groups()

                line = (line[:matchobj.start()]
                        + mark(*args)
                        + line[matchobj.end():])

        yield line


STATEMENTS = """
hello _date world _10e
expr::expl::test

.
"""

if __name__ == "__main__":
    for line in parse_inline(STATEMENTS):
        print(line)

    print("\n".join(parse_inline(STATEMENTS)))
