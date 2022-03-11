from pprint import pprint
from typing import Optional, Dict, List, Set
import first
import follow
import parse_table

rules: Dict[str, List[Optional[str]]] = {
    "E": ["TX"],
    "X": ["+TX", "-TX", None],
    "T": ["FY"],
    "Y": ["*FY", "/FY", None],
    "F": ["n", "i", "(E)"],
}

firsts: Dict[str, Set[Optional[str]]] = first.find_firsts(rules)
follows: Dict[str, Set[str]] = follow.find_follows(rules, firsts)
print("Firsts:")
pprint(firsts)
print("Follows:")
pprint(follows)
parse_tables = parse_table.parse_table(rules, firsts, follows)
print("Parsing table: ")
pprint(parse_tables)
