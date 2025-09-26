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

def test_positive_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_positive_single_digit_odd():
    assert even_odd_count(3) == (0, 1)

def test_zero():
    assert even_odd_count(0) == (1, 0)

def test_negative_single_digit_even():
    assert even_odd_count(-2) == (1, 0)

def test_negative_single_digit_odd():
    assert even_odd_count(-3) == (0, 1)

def test_positive_multiple_digits_all_even():
    assert even_odd_count(2468) == (4, 0)

def test_positive_multiple_digits_all_odd():
    assert even_odd_count(1357) == (0, 4)

def test_positive_multiple_digits_mixed():
    assert even_odd_count(12345) == (2, 3)

def test_negative_multiple_digits_all_even():
    assert even_odd_count(-2468) == (4, 0)

def test_negative_multiple_digits_all_odd():
    assert even_odd_count(-1357) == (0, 4)

def test_negative_multiple_digits_mixed():
    assert even_odd_count(-12345) == (2, 3)

def test_large_positive_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_large_negative_number():
    assert even_odd_count(-1234567890) == (5, 5)

def test_number_with_zeros():
    assert even_odd_count(10203) == (3, 2)

def test_negative_number_with_zeros():
    assert even_odd_count(-10203) == (3, 2)

@pytest.mark.parametrize("num,expected", [
    (1, (0, 1)),
    (4, (1, 0)),
    (10, (1, 1)),
    (11, (0, 2)),
    (123, (1, 2)),
    (246, (3, 0)),
    (135, (0, 3)),
    (-1, (0, 1)),
    (-4, (1, 0)),
    (-123, (1, 2)),
    (9876543210, (5, 5)),
    (-9876543210, (5, 5))
])
def test_parametrized_cases(num, expected):
    assert even_odd_count(num) == expected

def test_integer_input():
    assert even_odd_count(12) == (1, 1)

def test_negative_integer_input():
    assert even_odd_count(-12) == (1, 1)