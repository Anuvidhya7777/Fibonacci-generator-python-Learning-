def fibonacci(n):
    """
    Returns the nth Fibonacci number using recursion.
    Fibonacci series: 0, 1, 1, 2, 3, 5, 8, ...
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        print(f"Fibonacci({num}) = {fibonacci(num)}")
    except ValueError as e:
        print("Error:", e)
