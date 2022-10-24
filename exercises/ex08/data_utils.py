"""Dictionary related utility functions."""

__author__ = ""

# Define your functions below
from io import TextIOWrapper

def read_lines(filename: str) -> list[str]:
    """Read every line from filename into a list."""
    lines: list[str] = []
    file_handle: TextIOWrapper = open(filename, "r")
    for line in file_handle:
        line = line.lower()
        line = line.strip()
        lines.append(line)
    file_handle.close()
    return lines

shakespeare_lines: list[str] = read_lines("./shakespeare.txt")
print(len(shakespeare_lines))