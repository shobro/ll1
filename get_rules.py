from lib2to3.pgen2.token import OP
from pprint import pprint
from typing import Dict, List, Optional


def find_new_terminal_name(
    grammer: Dict[str, List[str]], new_grammer: Dict[str, List[str]]
) -> str:
    new_terminal_name = "A"
    while (
        new_terminal_name in grammer.keys() or new_terminal_name in new_grammer.keys()
    ):
        new_terminal_name = chr(ord(new_terminal_name) + 1)
    return new_terminal_name


def remove_left_recursion(
    grammer: Dict[str, List[Optional[str]]]
) -> Dict[str, List[str]]:
    new_grammer: Dict[str, List[str]] = dict()
    for left_side, right_side in grammer.items():
        left_recursive_productions = []
        if None in right_side:
            continue
        for production in right_side:
            if left_side == production[0]:
                left_recursive_productions.append(production)

        if left_recursive_productions:
            new_grammer[left_side] = []
            new_non_terminal = find_new_terminal_name(grammer, new_grammer)
            for production in right_side:
                if production not in left_recursive_productions:
                    new_grammer[left_side].append(production + new_non_terminal)

            new_grammer[new_non_terminal] = [None]
            for production in left_recursive_productions:
                new_grammer[new_non_terminal].append(production[1:] + new_non_terminal)
        else:
            new_grammer[left_side] = right_side

    return new_grammer


def get_grammer(file_name: str) -> Dict[str, List[Optional[str]]]:
    grammer: Dict[str, List[Optional[str]]] = dict()

    for line in open(file_name):
        left_side, right_side = line.split("->")
        right_side_list: List[str | None] = [s.strip() for s in right_side.split("|")]  # type: ignore
        for i, item in enumerate(right_side_list):
            if item == "eps":
                right_side_list[i] = None

        grammer[left_side.strip()] = right_side_list

    print("Grammer read as: ")
    pprint(grammer)

    return remove_left_recursion(grammer)