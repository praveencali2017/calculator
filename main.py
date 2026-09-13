"""A simple calculator MCP server built with FastMCP."""

from fastmcp import FastMCP

mcp = FastMCP("calculator")


@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@mcp.tool
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide a by b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


@mcp.tool
def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent."""
    return base ** exponent


@mcp.tool
def sqrt(value: float) -> float:
    """Return the square root of a non-negative number."""
    if value < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return value ** 0.5


if __name__ == "__main__":
    mcp.run()
