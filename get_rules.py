from pprint import pprint
from typing import Dict, List, Optional


def get_grammer(file_name) -> Dict[str, List[Optional[str]]]:
    grammer = dict()

    for line in open(file_name):
        left_side, right_side = line.split("->")
        right_side_list: List[str | None] = [s.strip() for s in right_side.split("|")]  # type: ignore
        for i, item in enumerate(right_side_list):
            if item == "eps":
                right_side_list[i] = None

        grammer[left_side.strip()] = right_side_list

    print("Rules parsed as: ")
    pprint(grammer)
    return grammer
