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

def test_sum_to_n_zero():
    assert sum_to_n(0) == 0

def test_sum_to_n_positive():
    assert sum_to_n(5) == 15
    assert sum_to_n(1) == 1
    assert sum_to_n(10) == 55

@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (2, 3),
    (3, 6),
    (4, 10),
    (5, 15),
    (10, 55),
    (100, 5050)
])
def test_sum_to_n_parametrized(n, expected):
    assert sum_to_n(n) == expected

def test_sum_to_n_large_number():
    assert sum_to_n(1000) == 500500

@pytest.mark.parametrize("invalid_input", [
    -1,
    -100,
    -999
])
def test_sum_to_n_negative_input(invalid_input):
    result = sum_to_n(invalid_input)
    assert result == 0

def test_sum_to_n_type_error():
    with pytest.raises(TypeError):
        sum_to_n("1")
    with pytest.raises(TypeError):
        sum_to_n([1, 2, 3])
    with pytest.raises(TypeError):
        sum_to_n(None)
    with pytest.raises(TypeError):
        sum_to_n(1.5)
