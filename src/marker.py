import textwrap
import time

from data import Config
from utils import capitalize, join, to_roman


class Alias:

    def abriged_date() -> str:
        return time.strftime("%d/%m/%y")

    def century(nb: str) -> str:
        return to_roman(int(nb))

    def line_numbering(nb: str) -> str:
        return f"(l.{nb})"


class Inline:

    def simple_definition(definition: str,
                          explanation: str) -> str:
        return f"{definition}{Config.simple_def_sep}{explanation}"

    def line_break() -> str:
        return Config.line_break


class Multiline:

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
        return text

    @capitalize
    def text_block(definition: str,
                   *explanations: str) -> str:
        left_offset = (len(definition) + 4)*" "

        fst_expl, *rest_expl = explanations
        header = f"{definition}{Config.text_block_sep}{fst_expl}"
        explanations = join(f"\n{left_offset}",
                            rest_expl)

        return f"{header}{explanations}"

    @capitalize
    def title(text: str,
              level: int) -> str:
        underlining = len(text)*Config.title_levels[level]

        return f"{text}\n{underlining}"
