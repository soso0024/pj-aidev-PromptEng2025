# Test cases for HumanEval/83
# Generated using Claude API


def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1: return 1
    return 18 * (10 ** (n - 2))


# Generated test cases:
import pytest

def starts_one_ends(n):
    if n == 1: return 1
    return 18 * (10 ** (n - 2))

def test_starts_one_ends_n_equals_1():
    assert starts_one_ends(1) == 1

def test_starts_one_ends_n_equals_2():
    assert starts_one_ends(2) == 18

def test_starts_one_ends_n_equals_3():
    assert starts_one_ends(3) == 180

def test_starts_one_ends_n_equals_4():
    assert starts_one_ends(4) == 1800

def test_starts_one_ends_n_equals_5():
    assert starts_one_ends(5) == 18000

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 18),
    (3, 180),
    (4, 1800),
    (5, 18000),
    (6, 180000),
    (10, 1800000000)
])
def test_starts_one_ends_parametrized(n, expected):
    assert starts_one_ends(n) == expected

def test_starts_one_ends_zero():
    assert starts_one_ends(0) == 0.18

def test_starts_one_ends_negative():
    result = starts_one_ends(-1)
    assert abs(result - 0.018) < 1e-10

def test_starts_one_ends_negative_large():
    result = starts_one_ends(-5)
    assert abs(result - 0.0000018) < 1e-10

def test_starts_one_ends_large_number():
    result = starts_one_ends(20)
    expected = 18 * (10 ** 18)
    assert result == expected

def test_starts_one_ends_float_input():
    assert starts_one_ends(2.0) == 18

def test_starts_one_ends_type_error():
    with pytest.raises(TypeError):
        starts_one_ends("string")

def test_starts_one_ends_type_error_none():
    with pytest.raises(TypeError):
        starts_one_ends(None)

def test_starts_one_ends_type_error_list():
    with pytest.raises(TypeError):
        starts_one_ends([1, 2, 3])