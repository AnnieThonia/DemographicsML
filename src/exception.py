# exception.py

def divide(a, b):
    """
    Divides two numbers.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If `b` is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
