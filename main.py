import argparse
from fibonacci.generator import fibonacci_n, fibonacci_upto

def main():
    parser = argparse.ArgumentParser(
        description="Fibonacci Generator CLI"
    )

    parser.add_argument(
        "--mode",
        choices=["n", "upto"],
        required=True,
        help="n = first N Fibonacci numbers, upto = up to max value"
    )

    parser.add_argument(
        "--value",
        type=int,
        required=True,
        help="Number of terms (mode=n) OR max value (mode=upto)"
    )

    args = parser.parse_args()

    if args.mode == "n":
        result = fibonacci_n(args.value)
    else:
        result = fibonacci_upto(args.value)

    for num in result:
        print(num)


if __name__ == "__main__":
    main()
