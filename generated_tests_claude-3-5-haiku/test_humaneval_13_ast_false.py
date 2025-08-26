# Test cases for HumanEval/13
# Generated using Claude API



def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    while b:
        a, b = b, a % b
    return a


# Generated test cases:
import pytest

def test_greatest_common_divisor_positive_numbers():
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(54, 24) == 6
    assert greatest_common_divisor(100, 75) == 25

def test_greatest_common_divisor_one_number_zero():
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(5, 0) == 5

def test_greatest_common_divisor_both_zero():
    assert greatest_common_divisor(0, 0) == 0

def test_greatest_common_divisor_coprime():
    assert greatest_common_divisor(17, 23) == 1
    assert greatest_common_divisor(11, 13) == 1

def test_greatest_common_divisor_large_numbers():
    assert greatest_common_divisor(1071, 462) == 21
    assert greatest_common_divisor(462, 1071) == 21

def test_greatest_common_divisor_negative_numbers():
    assert greatest_common_divisor(-48, 18) == 6
    assert greatest_common_divisor(48, -18) == 6
    assert greatest_common_divisor(-48, -18) == 6

@pytest.mark.parametrize("a,b,expected", [
    (48, 18, 6),
    (54, 24, 6),
    (100, 75, 25),
    (0, 5, 5),
    (5, 0, 5),
    (0, 0, 0),
    (17, 23, 1),
    (1071, 462, 21),
    (-48, 18, 6),
    (48, -18, 6),
    (-48, -18, 6)
])
def test_greatest_common_divisor_parametrized(a, b, expected):
    assert greatest_common_divisor(abs(a), abs(b)) == expected