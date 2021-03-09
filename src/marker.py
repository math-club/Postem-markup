import textwrap
import time

from data import Config
from utils import capitalize, join


class Alias:

    def abdridged_date() -> str:
        return time.strftime("%d/%m/%y")

    def line_numbering(nb: str) -> str:
        return f"(l.{nb})"

@capitalize
def complex_definition(definition: str,
                       explanation: str,
                       *justifications) -> str:
    header = f"{definition}{Config.complex_def_sep}{explanation}"
    justification = join(f"\n{Config.indent}{Config.complex_sep}",
                          justifications)

    return f"{header}{justification}"


def simple_definition(definition: str,
                      explanation: str) -> str:
    return f"{definition}{Config.simple_definition_separator}{explanation}"


def text_block(definition: str,
               *explanations: str) -> str:
    left_offset = (len(definition) + 4)*" "

    fst_expl, *rest_expl = explanations
    header = f"{definition}{Config.text_block_sep}{fst_expl}"
    explanations = join(f"\n{left_offset}",
                        rest_expl)

    return f"{header}{explanations}"
