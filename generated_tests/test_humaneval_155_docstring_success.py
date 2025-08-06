# Test cases for HumanEval/155
# Generated using Claude API


def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)


# Generated test cases:
import pytest

@pytest.mark.parametrize("num,expected", [
    (123, (1, 2)),
    (-12, (1, 1)),
    (0, (1, 0)),
    (2468, (4, 0)),
    (1357, (0, 4)),
    (-2468, (4, 0)),
    (-1357, (0, 4)),
    (1000, (3, 1)),
    (999999, (0, 6)),
    (42536, (3, 2)),
    (-42536, (3, 2)),
])
def test_even_odd_count_normal_cases(num, expected):
    assert even_odd_count(num) == expected

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_digit():
    assert even_odd_count(5) == (0, 1)
    assert even_odd_count(8) == (1, 0)

def test_even_odd_count_negative():
    assert even_odd_count(-5) == (0, 1)
    assert even_odd_count(-8) == (1, 0)

def test_even_odd_count_large_number():
    assert even_odd_count(1234567890) == (5, 5)

@pytest.mark.parametrize("num", [
    None,
    "123",
    [],
    {},
])
def test_even_odd_count_invalid_input(num):
    with pytest.raises((TypeError, AttributeError)):
        even_odd_count(num)

def test_even_odd_count_float():
    with pytest.raises(ValueError):
        even_odd_count(3.14)

def test_even_odd_count_bool():
    assert even_odd_count(True) == (0, 1)
    assert even_odd_count(False) == (1, 0)