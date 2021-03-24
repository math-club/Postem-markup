"""This module contains the parameters used for the generation of
Postem text.
"""

from typing import Tuple


class Config:
    indent: str = " "*2
    tabulation: str = " "*4
    line_break: str = "\n"*1

    date_format: str = "%d/%m/%y"

    capitalize: bool = True

    conclusion_beg: str = "=> "

    complex_def_sep: str = " -> "
    complex_just_beg: str = r"\-> "

    simple_def_sep: str = "->"

    text_block_sep: str = " -> "

    title_levels: Tuple[str] = (
        "#",
        "*",
        "=",
        "-",
        "^",
        '"'
    )
