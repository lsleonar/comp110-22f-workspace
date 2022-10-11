"""EX04 - `list` Utility Functions!"""


__author__ = "730621513"


def all(random_list: list[int], number: int) -> bool:
    """Given parameters will compare if the number in the list are the same as number and return True or False."""
    i = 0
    if len(random_list) == 0:
        return False
    while i < len(random_list):
        if random_list[i] == number:
            i += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Given paramter will return max of list."""
    i = 0
    max_value = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    for i in range(0, len(input), 1):
        if max_value < input[i]:
            max_value = input[i]
    return (max_value)


def is_equal(random_list: list[int], list2: list[int]) -> bool:
    """Given parameter will compare if lists are the same and return True or False."""
    i = 0
    if len(random_list) != len(list2):
        return False
    while i < len(random_list):
        if random_list[i] == list2[i]:
            i += 1
        else:
            return False
    return (True)