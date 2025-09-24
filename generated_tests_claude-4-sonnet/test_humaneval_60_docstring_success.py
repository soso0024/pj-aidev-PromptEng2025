# Test cases for HumanEval/60
# Generated using Claude API



def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """

    return sum(range(n + 1))


# Generated test cases:
import pytest

def sum_to_n(n: int):
    return sum(range(n + 1))

def test_sum_to_n_positive_numbers():
    assert sum_to_n(1) == 1
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050

def test_sum_to_n_zero():
    assert sum_to_n(0) == 0

def test_sum_to_n_negative_numbers():
    assert sum_to_n(-1) == 0
    assert sum_to_n(-5) == 0
    assert sum_to_n(-10) == 0

def test_sum_to_n_large_numbers():
    assert sum_to_n(1000) == 500500
    assert sum_to_n(999) == 499500

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 3),
    (3, 6),
    (4, 10),
    (5, 15),
    (6, 21),
    (7, 28),
    (8, 36),
    (9, 45),
    (10, 55)
])
def test_sum_to_n_parametrized(n, expected):
    assert sum_to_n(n) == expected

def test_sum_to_n_formula_verification():
    for n in [1, 5, 10, 20, 50, 100]:
        expected = n * (n + 1) // 2
        assert sum_to_n(n) == expected

def test_sum_to_n_type_handling():
    assert sum_to_n(int(5.0)) == 15
    assert sum_to_n(int(10.9)) == 55
