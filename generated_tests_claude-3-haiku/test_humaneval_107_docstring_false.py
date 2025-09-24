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
from your_module import even_odd_palindrome

import pytest

@pytest.mark.parametrize("n,expected", [
    (3, (1, 2)),
    (12, (4, 6)),
    (1, (0, 1)),
    (10, (3, 4)),
    (100, (25, 25)),
    (1000, (250, 250))
])
def test_even_odd_palindrome(n, expected):
    assert even_odd_palindrome(n) == expected

def test_even_odd_palindrome_negative_input():
    with pytest.raises(ValueError):
        even_odd_palindrome(-1)

def test_even_odd_palindrome_zero_input():
    with pytest.raises(ValueError):
        even_odd_palindrome(0)