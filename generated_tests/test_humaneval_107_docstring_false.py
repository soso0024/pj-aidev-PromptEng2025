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

def test_even_odd_palindrome_basic():
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(12) == (4, 6)

def test_even_odd_palindrome_single():
    assert even_odd_palindrome(1) == (0, 1)

def test_even_odd_palindrome_edge_cases():
    assert even_odd_palindrome(1000) == (48, 60)
    assert even_odd_palindrome(2) == (1, 1)

@pytest.mark.parametrize("input_n,expected", [
    (5, (2, 3)),
    (10, (4, 5)),
    (20, (4, 6)),
    (100, (8, 10)),
    (50, (6, 7)),
])
def test_even_odd_palindrome_parametrized(input_n, expected):
    assert even_odd_palindrome(input_n) == expected

@pytest.mark.parametrize("invalid_input", [
    0,
    -1,
    -100,
])
def test_even_odd_palindrome_invalid_input(invalid_input):
    try:
        even_odd_palindrome(invalid_input)
        pytest.fail("Expected ValueError for invalid input")
    except ValueError:
        pass

def test_even_odd_palindrome_specific_palindromes():
    assert even_odd_palindrome(11) == (4, 6)
    assert even_odd_palindrome(22) == (5, 6)
    assert even_odd_palindrome(99) == (8, 10)

def test_even_odd_palindrome_boundary():
    assert even_odd_palindrome(9) == (4, 5)
    assert even_odd_palindrome(100) == (8, 10)

def test_even_odd_palindrome_consecutive():
    result1 = even_odd_palindrome(8)
    result2 = even_odd_palindrome(9)
    result3 = even_odd_palindrome(10)
    assert result1 == (4, 4)
    assert result2 == (4, 5)
    assert result3 == (4, 5)