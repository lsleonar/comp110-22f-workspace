"""Examples of optional paramters and Union types."""

def hello(name: str = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, " + name
    return greeting

# Single argument
print(hello("sally"))

# No arguments
print(hello())