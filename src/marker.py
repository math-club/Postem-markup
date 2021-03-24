"""This module contains all the functions used for text formatting."""

import time

from data import Config
import parser
from utils import capitalize, join, to_roman


class Alias:
    """Encapsulates functions related to alias."""

    def abriged_date() -> str:
        return time.strftime(Config.date_format)

    def century(nb: str) -> str:
        return to_roman(int(nb))

    def line_numbering(nb: str) -> str:
        return f"(l.{nb})"


class Inline:
    """Encapsulates functions related to inline marks."""
    
    def simple_definition(definition: str,
                          explanation: str) -> str:
        return f"{definition}{Config.simple_def_sep}{explanation}"

    def line_break() -> str:
        return Config.line_break


class Multiline:
    """Encapsulates functions related to multiline tags."""
    
    @capitalize
    def conclusion(text: str) -> str:
        return f"{Config.conclusion_beg}{text}"

    @capitalize
    def complex_definition(definition: str,
                           explanation: str,
                           *justifications) -> str:
        header = f"{definition}{Config.complex_def_sep}{explanation}"
        justification = join(f"\n{Config.indent}{Config.complex_just_beg}",
                             justifications)

        return f"{header}{justification}"

    @capitalize
    def paragraph(text: str) -> str:
        return f"{Config.tabulation}{text}"

    @capitalize
    def text_block(definition: str,
                   *explanations: str) -> str:
        left_offset = (len(definition) + 4)*" "

        fst_expl, *rest_expl = explanations
        header = f"{definition}{Config.text_block_sep}{fst_expl}"
        explanations = join(f"\n{left_offset}",
                            rest_expl)

        return f"{header}{explanations}"

    @parser.parse_title
    @capitalize
    def title(text: str,
              level: int) -> str:
        underlining = len(text)*Config.title_levels[level]

        return f"{text}\n{underlining}"
