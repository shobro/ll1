from typing import Dict, List, Set

def parse_table(
    rules: Dict[str, List],
    first: Dict[str, Set],
    follow: Dict[str, Set],
):
    parse_table: Dict[str, Dict[str, str]] = dict()
    non_terminals: List[str] = list(rules.keys())

    def insert(non_terminal, terminal, rule):
        if terminal in parse_table[non_terminal]:
            print("Error: Ambiguous grammar")
            print(f"{non_terminal} -> {parse_table[non_terminal][terminal]} and {non_terminal} -> {rule} conflict") 
            exit(1)
        else:
            parse_table[non_terminal][terminal] = rule           

    for nt in rules.keys():
        parse_table[nt] = dict()

    for nonterminal in non_terminals:
        for rule in rules[nonterminal]:
            if rule == None:
                for follow_terminals in follow[nonterminal]:
                    insert(nonterminal, follow_terminals, rule)
                continue
            for ch in rule:
                flag: int = 0
                if ch not in non_terminals:
                    insert(nonterminal, ch, rule)
                    break
                else:
                    for first_set in first[ch]:
                        if first_set == None:
                            flag = 1
                            continue
                        insert(nonterminal, first_set, rule)
                if flag == 0:
                    break
                if ch == rule[len(rule) - 1]:
                    for follow_set in follow[nonterminal]:
                        insert(nonterminal, follow_set, rule)

    return parse_table
