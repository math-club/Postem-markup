import re


inline_marker = {
    r"_date": "Alias.abdridged_date"
    r"_([\d]+)e": "Alias.century"
    r"_([\d]+)": "Alias.line_numbering"
}


def lex(text: str):
    ...
