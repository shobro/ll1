from pprint import pprint
from typing import Optional


rules: dict[str, list[Optional[str]]] = {
    "E": ["TX"],
    "X": ["+TX", "-TX", None],
    "T": ["FY"],
    "Y": ["*FY", "/FY", None],
    "F": ["n", "i", "(E)"],
}


def is_terminal(c: str):
    return c in rules.keys()


firsts: dict[str, set[Optional[str]]] = dict()


def find_first(terminal: str) -> set[Optional[str]]:
    ret: set[Optional[str]] = set()
    for production in rules[terminal]:
        if production is None:
            ret.add(None)
        elif not is_terminal(production[0]):
            ret.add(production[0])
        else:
            ret |= find_first(production[0])
    return ret


for terminal in rules.keys():
    firsts[terminal] = find_first(terminal)

pprint(firsts)
