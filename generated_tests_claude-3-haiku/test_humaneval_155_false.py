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
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

def test_even_odd_count_positive_number():
    assert even_odd_count(12345) == (2, 3)

def test_even_odd_count_negative_number():
    assert even_odd_count(-12345) == (2, 3)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_digit_even():
    assert even_odd_count(8) == (1, 0)

def test_even_odd_count_single_digit_odd():
    assert even_odd_count(7) == (0, 1)

@pytest.mark.parametrize("input,expected", [
    (123456789, (5, 4)),
    (-987654321, (5, 4)),
    (0, (1, 0)),
    (2, (1, 0)),
    (3, (0, 1)),
    (-2, (1, 0)),
    (-3, (0, 1)),
])
def test_even_odd_count_parametrized(input, expected):
    assert even_odd_count(input) == expected