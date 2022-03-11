from typing import Dict, List, Optional, Set


def find_follow(
    non_terminal: str,
    non_terminals: List[str],
    rules: Dict[str, List[Optional[str]]],
    firsts: Dict[str, Set[Optional[str]]],
) -> Set[str]:
    ret: Set[Optional[str]] = set()

    for left_side, right_side in rules.items():
        for production in right_side:
            if production is None or non_terminal not in production:
                continue  # if production is Epsilon

            i = production.index(non_terminal) + 1
            # TODO: does not work if `non-terminal` is present multiple times in
            # `production`
            while i < len(production):
                token: str = production[i]

                if token not in non_terminals:
                    ret.add(token)
                    break
                else:
                    ret |= firsts[token]
                    if None in firsts[token]:
                        ret.remove(None)
                    else:
                        break

                i += 1

            if i == len(production) and non_terminal != left_side:
                ret |= find_follow(left_side, non_terminals, rules, firsts)

    assert None not in ret
    if non_terminal == non_terminals[0]:
        ret.add("$")
    return ret


def find_follows(
    rules: Dict[str, List[Optional[str]]], firsts: Dict[str, Set[Optional[str]]]
) -> Dict[str, Set[str]]:
    follow_set: Dict[str, Set[str]] = dict()
    non_terminals: List[str] = list(rules.keys())

    for non_terminal in non_terminals:
        if non_terminal in follow_set:
            follow_set[non_terminal] |= find_follow(
                non_terminal, non_terminals, rules, firsts
            )
        else:
            follow_set[non_terminal] = find_follow(
                non_terminal, non_terminals, rules, firsts
            )

    return follow_set
