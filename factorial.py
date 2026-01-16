def factorial_loop(n):
    """
    Returns factorial of n using a loop
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
#loop method

def factorial_recursive(n):
    """
    Returns factorial of n using recursion
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)
#recursive method

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))

        print(f"Factorial (loop) of {num} = {factorial_loop(num)}")
        print(f"Factorial (recursion) of {num} = {factorial_recursive(num)}")

    except ValueError as e:
        print("Error:", e)

#time complexity - O(n)