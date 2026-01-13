def fibonacci_n(n):
    """Generate first n Fibonacci numbers."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")

    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fibonacci_upto(max_value):
    """Generate Fibonacci numbers up to max_value."""
    if not isinstance(max_value, int):
        raise TypeError("max_value must be an integer")
    if max_value < 0:
        raise ValueError("max_value must be non-negative")

    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b
