from pprint import pprint
from typing import Optional, Dict, List, Set
import first
import follow
import parse_table
import parsing
import get_rules


grammer = get_rules.get_grammer("grammer.txt")
print("Rules parsed as: ")
pprint(grammer)

firsts = first.find_firsts(grammer)
print("Firsts:")
pprint(firsts)

follows = follow.find_follows(grammer, firsts)
print("Follows:")
pprint(follows)

parse_tables = parse_table.parse_table(grammer, firsts, follows)
print("Parsing table: ")
pprint(parse_tables)

parsing.parsing(grammer, parse_tables)
