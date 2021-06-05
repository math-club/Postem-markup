"""This module contains the filtering patterns for each tag and the
functions useful for compilation.
"""

import re
from re import Pattern
from typing import Any, Callable, Dict, Generator, Tuple

from .data import Config
from .marker import Alias, Inline, Multiline
from .logger import logger


Regex = str
MarkedText = str

text = r"[^\n]"
numeric = r"\d"
space = r"[ \t]"

inline_marks: Dict[Regex, Callable] = {
    "_date": Alias.abriged_date,
    fr"_({numeric}+){Config.century_suffix}": Alias.century,
    fr"_({numeric}+)[^{Config.century_suffix}]": Alias.line_numbering,
    r"({text}+){space}*::{space}*({text}+)": Inline.simple_definition,
}

multiline_marks: Dict[Regex, Callable] = {
    r"^\.\.{space}*({text}*)$": Multiline.conclusion,
    r"^(&{1,6}){space}*({text}+)$": Multiline.title
}


def compiles(iterable: Dict[Regex, Any]) -> Dict[Pattern, Any]:
    """Returns the given dictionary with these compiled keys."""
    return {re.compile(key): value
                for key, value in iterable.items()}


def parse_inline(text: str,
                 verbose: bool) -> Generator[str, None, None]:
    patterns = compiles(inline_marks)

    for nb, line in enumerate(text.split("\n"), 1):
        line_chunck = []

        for pattern, mark in patterns.items():
            for matchobj in pattern.finditer(line):
                args = matchobj.groups()

                # line_chunck.append(line[:matchobj.start()])
                line_chunck.append(mark(*args))
                line_chunck.append(line[matchobj.end():])

                logger.debug(mark(*args))
                # parsed_line = (line[:matchobj.start()]
                #                + mark(*args)
                #                + line[matchobj.end():])

                if verbose:
                    logger.info(f"line {nb} :: "
                                f"mark {mark.__name__} parsed.")

        yield "".join(line_chunck)


def parse_multine(lines: Generator, verbose: bool) -> str:
    return "\n".join(lines)


def parse(text: MarkedText, verbose: bool = False) -> str:
    return parse_multine(parse_inline(text, verbose),
                         verbose)


STATEMENTS = """
hello _date world _10e
expr::expl::test

.
"""

if __name__ == "__main__":
    print(parse(STATEMENTS))
