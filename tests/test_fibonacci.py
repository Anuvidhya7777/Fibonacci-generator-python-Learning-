from fibonacci.generator import fibonacci_n

def test_fibonacci():
    assert list(fibonacci_n(5)) == [0, 1, 1, 2, 3]
