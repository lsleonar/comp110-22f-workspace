"""Ex07 dictionary test file."""


__author__ = "730621513"


from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_invert_1() -> None:
    """Gives dictionary to test invert function."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_2() -> None:
    """Gives dictionary to test invert function."""
    xs: dict[str, str] = {'b': 't'}
    assert invert(xs) == {'t': 'b'}


def test_invert_3() -> None:
    """Tests invert for edge case of empty dictionary."""
    assert invert({}) == {}


def test_favorite_color_1() -> None:
    """Gives dictionary to test favorite_color function."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_2() -> None:
    """Gives dictionary to test favorite_color function."""
    assert favorite_color({"Lauren": "yellow"}) == "yellow"


def test_favorite_color_empty() -> None:
    """Tests favorite_color for edge case of empty dictionary."""
    assert favorite_color({}) == ""


def test_count_1() -> None:
    """Gives list to test count function."""
    assert count(["y", "o", "u"]) == {"y": 1, "o": 1, "u": 1}


def test_count_2() -> None:
    """Gives list to test count function."""
    assert count(["t", "u", "b"]) == {"t": 1, "u": 1, "b": 1}


def test_count_empty() -> None:
    """Tests count for edge case of empty list."""
    assert count([]) == {}