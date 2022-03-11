from typing import Dict, List, Optional, Set


def is_terminal(token: str, rules: Dict[str, List[Optional[str]]]):
    return token not in rules.keys()


def find_first(
    non_terminal: str, rules: Dict[str, List[Optional[str]]]
) -> Set[Optional[str]]:
    ret: Set[Optional[str]] = set()
    for production in rules[non_terminal]:
        if production is None:
            ret.add(None)
        elif is_terminal(production[0], rules):
            ret.add(production[0])
        else:
            ret |= find_first(production[0], rules)
    return ret


def find_firsts(rules: Dict[str, List[Optional[str]]]) -> Dict[str, Set[Optional[str]]]:
    firsts: Dict[str, Set[Optional[str]]] = dict()

    for non_terminal in rules.keys():
        firsts[non_terminal] = find_first(non_terminal, rules)

    return firsts
