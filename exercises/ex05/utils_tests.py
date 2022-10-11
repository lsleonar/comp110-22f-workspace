"""Ex05 Utils tets."""


__author__ = "730621513"


from utils import only_evens


def test_only_evens_1() -> None:
    """Tests for list."""
    assert only_evens([]) == []