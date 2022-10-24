"""Ex07 Dictionary Functions."""


__author__ = "730621513"


def invert(dict_input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values."""
    invert: dict[str, str] = {}
    for key in dict_input:
        if dict_input[key] in invert:
            raise KeyError("Duplicate key")
        invert[dict_input[key]] = key
    return invert


def favorite_color(dict_input: dict[str, str]) -> str:
    """Given dictionary returns a str which is the color that appears most frequently."""
    favorite_color: dict[str, int] = {}
    curr_color: str = ""
    max: int = 0
    color: str = ""
    for name in dict_input:
        curr_color = dict_input[name]
        if (curr_color in favorite_color):
            favorite_color[curr_color] += 1
        else: 
            favorite_color[curr_color] = 1
    for name in favorite_color:
        if favorite_color[name] > max:
            max = favorite_color[name]
            color = name
    return color
        

def count(random_list: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    empty_dict: dict[str, int] = {}
    for item in random_list:
        if item in empty_dict:
            empty_dict[item] += 1
        else:
            empty_dict[item] = 1
    return empty_dict
