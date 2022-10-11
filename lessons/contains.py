"""Example implementing a list utility function."""

def conatins(needle: str, haystack: list[str]) -> bool:
    i: int = 0
    while i< len(haystack):
        if haystack [i] == needle:
            return True
        i += 1

    return False