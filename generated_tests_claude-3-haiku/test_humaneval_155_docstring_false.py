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
from your_module import even_odd_count

import pytest

@pytest.mark.parametrize("num,expected", [
    (0, (1, 0)),
    (1, (0, 1)),
    (-12, (1, 1)),
    (123, (1, 2)),
    (1234567890, (5, 5)),
    (-987654321, (0, 10)),
    (100000, (6, 0)),
    (-111111, (0, 6)),
    (42, (1, 1)),
    (-24, (2, 0))
])
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)

def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)