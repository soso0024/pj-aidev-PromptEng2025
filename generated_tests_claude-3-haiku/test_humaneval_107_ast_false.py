# Test cases for HumanEval/107
# Generated using Claude API


def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n+1):
        if i%2 == 1 and is_palindrome(i):
                odd_palindrome_count += 1
        elif i%2 == 0 and is_palindrome(i):
            even_palindrome_count += 1
    return (even_palindrome_count, odd_palindrome_count)


# Generated test cases:
import pytest

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def even_odd_palindrome(n):
    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n+1):
        if i%2 == 1 and is_palindrome(i):
            odd_palindrome_count += 1
        elif i%2 == 0 and is_palindrome(i):
            even_palindrome_count += 1
    return (even_palindrome_count, odd_palindrome_count)

def test_even_odd_palindrome():
    assert even_odd_palindrome(10) == (4, 4)
    assert even_odd_palindrome(20) == (8, 6)
    assert even_odd_palindrome(0) == (0, 0)
    assert even_odd_palindrome(-5) == (0, 0)

@pytest.mark.parametrize("input,expected", [
    (10, (4, 4)),
    (20, (8, 6)),
    (0, (0, 0)),
    (-5, (0, 0)),
    (100, (24, 25)),
    (1000, (248, 251))
])
def test_even_odd_palindrome_parametrized(input, expected):
    assert even_odd_palindrome(input) == expected

def test_is_palindrome():
    assert is_palindrome(121) is True
    assert is_palindrome(12321) is True
    assert is_palindrome(123) is False
    assert is_palindrome(0) is True
    assert is_palindrome(-1) is False

@pytest.mark.parametrize("input,expected", [
    (121, True),
    (12321, True),
    (123, False),
    (0, True),
    (-1, False),
    ('racecar', True),
    ('level', True),
    ('hello', False)
])
def test_is_palindrome_parametrized(input, expected):
    assert is_palindrome(input) == expected