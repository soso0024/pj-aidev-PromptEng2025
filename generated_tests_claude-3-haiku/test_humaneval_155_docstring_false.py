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
from math import fabs

@pytest.mark.parametrize("num,expected", [
    (0, (1, 0)),
    (1, (0, 1)),
    (-12, (1, 1)),
    (123, (1, 2)),
    (1000, (4, 0)),
    (-4321, (2, 2)),
    (10000, (5, 0)),
    (-98765, (3, 5)),
    (1234567890, (5, 5)),
    (-0, (1, 0)),
    (100, (3, 0)),
    (-100, (3, 0)),
    (101, (1, 2)),
    (-101, (1, 2)),
    (1000000000000000000, (19, 0)),
    (-1000000000000000000, (19, 0)),
])
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected