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

def test_even_odd_count_positive_number():
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_negative_number():
    assert even_odd_count(-12) == (1, 1)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_all_even():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_all_odd():
    assert even_odd_count(13579) == (0, 5)

@pytest.mark.parametrize("input_num,expected", [
    (123, (1, 2)),
    (-12, (1, 1)),
    (0, (1, 0)),
    (2468, (4, 0)),
    (13579, (0, 5)),
    (1010, (4, 0)),
    (-9876, (4, 0))
])
def test_even_odd_count_parametrized(input_num, expected):
    assert even_odd_count(input_num) == expected