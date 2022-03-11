from pprint import pprint
from typing import Optional, Dict, List, Set
import first

rules: Dict[str, List[Optional[str]]] = {
    "E": ["TX"],
    "X": ["+TX", "-TX", None],
    "T": ["FY"],
    "Y": ["*FY", "/FY", None],
    "F": ["n", "i", "(E)"],
}

firsts: Dict[str, Set[Optional[str]]] = first.find_firsts(rules)

pprint(firsts)
