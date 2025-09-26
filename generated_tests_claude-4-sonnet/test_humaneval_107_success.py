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
        if i%2 == 1 and is_palindrome(i):
                odd_palindrome_count += 1
        elif i%2 == 0 and is_palindrome(i):
            even_palindrome_count += 1
    return (even_palindrome_count, odd_palindrome_count)

def test_even_odd_palindrome_edge_case_zero():
    assert even_odd_palindrome(0) == (0, 0)

def test_even_odd_palindrome_edge_case_one():
    assert even_odd_palindrome(1) == (0, 1)

def test_even_odd_palindrome_edge_case_two():
    assert even_odd_palindrome(2) == (1, 1)

def test_even_odd_palindrome_small_numbers():
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(4) == (2, 2)
    assert even_odd_palindrome(5) == (2, 3)

def test_even_odd_palindrome_ten():
    assert even_odd_palindrome(10) == (4, 5)

def test_even_odd_palindrome_eleven():
    assert even_odd_palindrome(11) == (4, 6)

def test_even_odd_palindrome_twenty():
    assert even_odd_palindrome(20) == (4, 6)

def test_even_odd_palindrome_hundred():
    assert even_odd_palindrome(100) == (8, 10)

def test_even_odd_palindrome_larger_number():
    assert even_odd_palindrome(123) == (8, 13)

@pytest.mark.parametrize("n,expected", [
    (1, (0, 1)),
    (2, (1, 1)),
    (3, (1, 2)),
    (4, (2, 2)),
    (5, (2, 3)),
    (6, (3, 3)),
    (7, (3, 4)),
    (8, (4, 4)),
    (9, (4, 5)),
    (10, (4, 5)),
    (11, (4, 6)),
    (22, (5, 6)),
    (33, (5, 7)),
    (44, (6, 7)),
    (55, (6, 8)),
    (99, (8, 10)),
    (101, (8, 11)),
    (111, (8, 12)),
    (121, (8, 13)),
    (131, (8, 14)),
    (141, (8, 15)),
    (151, (8, 16))
])
def test_even_odd_palindrome_parametrized(n, expected):
    assert even_odd_palindrome(n) == expected

def test_even_odd_palindrome_negative_number():
    result = even_odd_palindrome(-1)
    assert result == (0, 0)

def test_even_odd_palindrome_large_number():
    result = even_odd_palindrome(1000)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
    assert all(x >= 0 for x in result)