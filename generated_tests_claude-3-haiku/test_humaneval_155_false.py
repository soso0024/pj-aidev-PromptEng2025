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
from even_odd_count import even_odd_count
import pytest

def test_even_odd_count_positive_number():
    assert even_odd_count(12345) == (3, 2)

def test_even_odd_count_negative_number():
    assert even_odd_count(-12345) == (3, 2)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_digit_even():
    assert even_odd_count(8) == (1, 0)

def test_even_odd_count_single_digit_odd():
    assert even_odd_count(7) == (0, 1)

@pytest.mark.parametrize("input,expected", [
    ('12345', (3, 2)),
    ('-12345', (3, 2)),
    ('0', (1, 0)),
    ('8', (1, 0)),
    ('7', (0, 1))
])
def test_even_odd_count_parametrized(input, expected):
    assert even_odd_count(int(input)) == expected

def test_even_odd_count_string_input():
    with pytest.raises(ValueError):
        even_odd_count('abc')