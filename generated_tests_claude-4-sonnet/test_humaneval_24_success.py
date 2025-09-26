# Test cases for HumanEval/24
# Generated using Claude API



def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    for i in reversed(range(n)):
        if n % i == 0:
            return i


# Generated test cases:
import pytest

def largest_divisor(n: int) -> int:
    for i in reversed(range(n)):
        if n % i == 0:
            return i

def test_largest_divisor_prime_numbers():
    assert largest_divisor(2) == 1
    assert largest_divisor(3) == 1
    assert largest_divisor(5) == 1
    assert largest_divisor(7) == 1
    assert largest_divisor(11) == 1
    assert largest_divisor(13) == 1

def test_largest_divisor_composite_numbers():
    assert largest_divisor(4) == 2
    assert largest_divisor(6) == 3
    assert largest_divisor(8) == 4
    assert largest_divisor(9) == 3
    assert largest_divisor(10) == 5
    assert largest_divisor(12) == 6
    assert largest_divisor(15) == 5
    assert largest_divisor(16) == 8
    assert largest_divisor(18) == 9
    assert largest_divisor(20) == 10

def test_largest_divisor_perfect_squares():
    assert largest_divisor(4) == 2
    assert largest_divisor(9) == 3
    assert largest_divisor(16) == 8
    assert largest_divisor(25) == 5
    assert largest_divisor(36) == 18
    assert largest_divisor(49) == 7
    assert largest_divisor(64) == 32
    assert largest_divisor(81) == 27
    assert largest_divisor(100) == 50

def test_largest_divisor_large_numbers():
    assert largest_divisor(100) == 50
    assert largest_divisor(144) == 72
    assert largest_divisor(200) == 100
    assert largest_divisor(1000) == 500

@pytest.mark.parametrize("n,expected", [
    (2, 1),
    (4, 2),
    (6, 3),
    (8, 4),
    (10, 5),
    (12, 6),
    (14, 7),
    (15, 5),
    (21, 7),
    (24, 12)
])
def test_largest_divisor_parametrized(n, expected):
    assert largest_divisor(n) == expected

def test_largest_divisor_edge_case_one():
    with pytest.raises(ZeroDivisionError):
        largest_divisor(1)

def test_largest_divisor_edge_case_zero():
    assert largest_divisor(0) is None

def test_largest_divisor_negative_numbers():
    assert largest_divisor(-1) is None
    assert largest_divisor(-5) is None
    assert largest_divisor(-10) is None

def test_largest_divisor_powers_of_two():
    assert largest_divisor(2) == 1
    assert largest_divisor(4) == 2
    assert largest_divisor(8) == 4
    assert largest_divisor(16) == 8
    assert largest_divisor(32) == 16
    assert largest_divisor(64) == 32
    assert largest_divisor(128) == 64

def test_largest_divisor_powers_of_three():
    assert largest_divisor(3) == 1
    assert largest_divisor(9) == 3
    assert largest_divisor(27) == 9
    assert largest_divisor(81) == 27