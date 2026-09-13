"""A simple calculator MCP server built with FastMCP.

This module exposes a small set of arithmetic tools over the Model Context
Protocol (MCP). Any MCP client (e.g. Claude Desktop, the FastMCP CLI, or a
custom Python client) can connect to this server and call the tools below to
perform basic mathematical operations.

Run the server (stdio transport) with:

    uv run python main.py
"""

from fastmcp import FastMCP

# A FastMCP application instance. The string "calculator" becomes the
# server's name, which clients see when they connect.
mcp = FastMCP("calculator")


@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: The first addend (any real number).
        b: The second addend (any real number).

    Returns:
        The sum of ``a`` and ``b``.

    Example:
        >>> add(2, 3)
        5.0
    """
    return a + b


@mcp.tool
def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first.

    Args:
        a: The minuend (the number to subtract from).
        b: The subtrahend (the number to subtract).

    Returns:
        The result of ``a - b``.

    Example:
        >>> subtract(10, 4)
        6.0
    """
    return a - b


@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: The first factor.
        b: The second factor.

    Returns:
        The product of ``a`` and ``b``.

    Example:
        >>> multiply(6, 7)
        42.0
    """
    return a * b


@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide the first number by the second.

    Args:
        a: The dividend (the number to be divided).
        b: The divisor (the number to divide by). Must be non-zero.

    Returns:
        The quotient ``a / b``.

    Raises:
        ZeroDivisionError: If ``b`` is zero.

    Example:
        >>> divide(10, 2)
        5.0
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


@mcp.tool
def power(base: float, exponent: float) -> float:
    """Raise a base to a given exponent.

    Args:
        base: The number to be raised to a power.
        exponent: The power to raise ``base`` to. Can be fractional
            (e.g. ``0.5`` for square root) or negative (for reciprocal powers).

    Returns:
        ``base ** exponent``.

    Example:
        >>> power(2, 10)
        1024.0
    """
    return base ** exponent


@mcp.tool
def sqrt(value: float) -> float:
    """Return the (principal) square root of a non-negative number.

    Args:
        value: The number whose square root is required. Must be >= 0.

    Returns:
        The non-negative square root of ``value``.

    Raises:
        ValueError: If ``value`` is negative.

    Example:
        >>> sqrt(25)
        5.0
    """
    if value < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return value ** 0.5


if __name__ == "__main__":
    # Start the MCP server. By default FastMCP runs over the stdio
    # transport, which is what MCP clients like Claude Desktop expect.
    mcp.run()
