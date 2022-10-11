"""Utils Ex05."""


__author__ = "730621513"


def only_evens(list_1: list[int]) -> list[int]:
    """Given parameters only_evens should return a new list containing only the elements of the input list that were even."""
    i = 0
    even = []
    while i < len(list_1):
        if list_1[i] % 2 == 0:
            even.append(list_1[i])
        i += 1
    return even 


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Given parameters, concat should generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    i = 0
    new_list = []
    while i < len(list_1):
        new_list.append(list_1[i])
        i += 1
    i = 0
    while i < len(list_2):
        new_list.append(list_2[i])
        i += 1
    return new_list


def sub(list_1: list[int], start_index: int, end_index: int) -> list[int]:
    """Given parameters will generate a List which is a subset of the given list, between the specified start index and the end index - 1."""
    new_list = []
    i = start_index
    end_index -= 1
    if i < 0:
        i = 0
    if len(list_1) == 0 or i > len(list_1) - 1:
        return new_list
    if end_index >= len(list_1):
        end_index = len(list_1) - 1
    while i <= end_index:
        new_list.append(list_1[i])
        i += 1
    return new_list