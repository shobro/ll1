from pprint import pprint
from typing import Dict, List, Set


def parse_table(
    rules: Dict[str, List],
    first: Dict[str, Set],
    follow: Dict[str, Set],
):
    parse_table: Dict[str, Dict[str, List]] = dict()
    non_terminals: Set[str] = set()

    for nt in rules.keys():
        non_terminals.add(nt)
        parse_table[nt] = dict()

    terminals: Set[str] = set()

    for nt in rules.keys():
        for r in rules[nt]:
            if r == None:
                terminals.add("$")
                continue
            for ch in r:
                if ch not in non_terminals:
                    terminals.add(ch)

    for nt in non_terminals:
        parse_table[nt] = dict()
        for t in terminals:
            parse_table[nt][t] = []

    for nonterminal in rules.keys():
        for rule in rules[nonterminal]:
            if rule == None:
                for follow_terminals in follow[nonterminal]:
                    parse_table[nonterminal][follow_terminals].append(rule)
                continue
            for ch in rule:
                flag: int = 0
                if ch in terminals:
                    parse_table[nonterminal][ch].append(rule)
                    break
                else:
                    print(type(first))
                    for first_set in first[ch]:
                        if first_set == None:
                            flag = 1
                            continue
                        parse_table[nonterminal][first_set].append(rule)
                if flag == 0:
                    break
                if ch == rule[len(rule) - 1]:
                    for follow_set in follow[nonterminal]:
                        parse_table[nonterminal][follow_set].append(rule)

    return parse_table
