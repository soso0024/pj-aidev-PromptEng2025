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

def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)

@pytest.mark.parametrize("num,expected", [
    (0, (1, 0)),
    (1, (0, 1)),
    (2, (1, 0)),
    (12, (1, 1)),
    (-12, (1, 1)),
    (123, (1, 2)),
    (-123, (1, 2)),
    (1234, (2, 2)),
    (-1234, (2, 2)),
    (13579, (0, 5)),
    (-13579, (0, 5)),
    (2468, (4, 0)),
    (-2468, (4, 0)),
    (1357924680, (5, 5)),
    (-1357924680, (5, 5)),
    (999, (0, 3)),
    (888, (3, 0)),
    (10203, (3, 2)),
    (-10203, (3, 2)),
    (5050505, (3, 4)),
    (-5050505, (3, 4))
])
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected

def test_single_digit_even():
    assert even_odd_count(4) == (1, 0)
    assert even_odd_count(6) == (1, 0)
    assert even_odd_count(8) == (1, 0)

def test_single_digit_odd():
    assert even_odd_count(3) == (0, 1)
    assert even_odd_count(5) == (0, 1)
    assert even_odd_count(7) == (0, 1)
    assert even_odd_count(9) == (0, 1)

def test_negative_single_digit():
    assert even_odd_count(-4) == (1, 0)
    assert even_odd_count(-7) == (0, 1)

def test_large_numbers():
    assert even_odd_count(1234567890) == (5, 5)
    assert even_odd_count(-1234567890) == (5, 5)

def test_all_zeros():
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(1000) == (3, 1)
    assert even_odd_count(-2000) == (4, 0)
