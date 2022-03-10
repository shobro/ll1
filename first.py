from pprint import pprint
from typing import Dict, Optional, Set


def is_terminal(c: str, rules: Dict):
    return c in rules.keys()


def find_first(terminal: str, rules: Dict) -> Set[Optional[str]]:
    ret: set[Optional[str]] = set()
    for production in rules[terminal]:
        if production is None:
            ret.add(None)
        elif not is_terminal(production[0], rules):
            ret.add(production[0])
        else:
            ret |= find_first(production[0], rules)
    return ret
