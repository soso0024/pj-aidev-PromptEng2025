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

def test_even_odd_count_positive():
    assert even_odd_count(123456) == (3, 3)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_negative():
    assert even_odd_count(-123456) == (3, 3)
    assert even_odd_count(-2468) == (4, 0)
    assert even_odd_count(-13579) == (0, 5)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_digit():
    assert even_odd_count(1) == (0, 1)
    assert even_odd_count(2) == (1, 0)

@pytest.mark.parametrize("num,expected", [
    (123456, (3, 3)),
    (-123456, (3, 3)),
    (2468, (4, 0)),
    (-2468, (4, 0)),
    (13579, (0, 5)),
    (-13579, (0, 5)),
    (0, (1, 0)),
    (1, (0, 1)),
    (2, (1, 0)),
    (999999, (0, 6)),
    (-999999, (0, 6)),
    (888888, (6, 0)),
    (-888888, (6, 0)),
])
def test_even_odd_count_parametrized(num, expected):
    assert even_odd_count(num) == expected

def test_even_odd_count_large_numbers():
    assert even_odd_count(1234567890) == (5, 5)
    assert even_odd_count(-1234567890) == (5, 5)

def test_even_odd_count_repeated_digits():
    assert even_odd_count(111111) == (0, 6)
    assert even_odd_count(222222) == (6, 0)
