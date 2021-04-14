"""This module contains the filtering patterns for each tag and the
functions useful for compilation.
"""

import re
from typing import Any, Callable, Dict, Generator, Tuple

from .marker import Alias, Inline, Multiline
from .logger import logger


Regex = str
MarkedText = str

inline_marks: Dict[Regex, Callable] = {
    r"_date": Alias.abriged_date,
    r"_([\d]+)e": Alias.century,
    r"_([\d]+)[^e]": Alias.line_numbering,
    r"([^\n]+)[ \t]*::[ \t]*([^\n]+)": Inline.simple_definition,
    # r"([\S\s]*)": Inline.text,
}

multiline_marks: Dict[Regex, Callable] = {
    r"^\.\.[ \t]*([^\n]+)$": Multiline.conclusion,
    r"^(&{1,6})[ \t]*([^\n]+)$": Multiline.title
}


def compiles(iterable: Dict[Regex, Any]) -> Dict[re.Pattern, Any]:
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
