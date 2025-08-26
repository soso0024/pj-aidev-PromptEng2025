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

def even_odd_palindrome(n):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n+1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_palindrome_count += 1
            else:
                odd_palindrome_count += 1
    return (even_palindrome_count, odd_palindrome_count)

def test_even_odd_palindrome_basic_cases():
    assert even_odd_palindrome(10) == (2, 3)
    assert even_odd_palindrome(20) == (4, 6)

def test_even_odd_palindrome_zero_input():
    assert even_odd_palindrome(0) == (0, 0)

def test_even_odd_palindrome_single_digit():
    assert even_odd_palindrome(5) == (0, 3)

@pytest.mark.parametrize("input_n,expected_even,expected_odd", [
    (1, 0, 1),
    (5, 0, 3),
    (10, 2, 3),
    (20, 4, 6),
    (100, 18, 30)
])
def test_even_odd_palindrome_parametrized(input_n, expected_even, expected_odd):
    result = even_odd_palindrome(input_n)
    assert result[0] == expected_even
    assert result[1] == expected_odd

def test_even_odd_palindrome_large_input():
    result = even_odd_palindrome(1000)
    assert result[0] > 0
    assert result[1] > 0

def test_even_odd_palindrome_return_type():
    result = even_odd_palindrome(10)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)