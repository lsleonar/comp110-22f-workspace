"""Ex07 Dictionary Functions."""

__author__ = "730621513"


def invert(dict_input: dict[str, str]) -> dict[str, str]:
    invert: dict[str, str] = {}
    for key in dict_input:
        if dict_input[key] in invert:
            raise KeyError("Duplicate key")
        invert[dict_input[key]] = key
    return invert

def favorite_color(dict_input: dict[str, str]) -> str:
   favorite_color: dict[str, str] = {}
   for dict_input[key] in favorite_color:
    i = 0
    i += 1

def count(random_list: list[int]) -> dict[str, int]:
    empty_dict: dict[str, str] = {}
    
