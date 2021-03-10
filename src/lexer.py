import re


inline_marks = {
    r"_date": "Alias.abriged_date",
    r"_([\d]+)e": "Alias.century",
    r"_([\d]+)": "Alias.line_numbering"
}

multiline_marks = {
    r"^\.\.[ \t]*([^\n]+)$": "Multiline.conclusion",
    r"^>{1,6}[ \t]*([^\n]+)$": "Multiline.title"
}


def lex(text: str):
    ...
