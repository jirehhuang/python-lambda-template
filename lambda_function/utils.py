"""Utility functions for the Lambda function."""


def format_greeting(name: str) -> str:
    """Format a friendly greeting.

    Args:
        name (str): Name to include in the greeting.

    Returns:
        str: Formatted greeting string.
    """
    return f"Hello from {name}!"
