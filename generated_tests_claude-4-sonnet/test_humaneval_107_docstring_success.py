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

def test_even_odd_palindrome_example_1():
    assert even_odd_palindrome(3) == (1, 2)

def test_even_odd_palindrome_example_2():
    assert even_odd_palindrome(12) == (4, 6)

def test_even_odd_palindrome_edge_case_1():
    assert even_odd_palindrome(1) == (0, 1)

def test_even_odd_palindrome_edge_case_2():
    assert even_odd_palindrome(2) == (1, 1)

def test_even_odd_palindrome_single_digit():
    assert even_odd_palindrome(9) == (4, 5)

def test_even_odd_palindrome_includes_11():
    assert even_odd_palindrome(11) == (4, 6)

def test_even_odd_palindrome_includes_22():
    assert even_odd_palindrome(22) == (5, 6)

def test_even_odd_palindrome_larger_range():
    assert even_odd_palindrome(100) == (8, 10)

def test_even_odd_palindrome_includes_33():
    assert even_odd_palindrome(33) == (5, 7)

def test_even_odd_palindrome_includes_44():
    assert even_odd_palindrome(44) == (6, 7)

def test_even_odd_palindrome_includes_99():
    assert even_odd_palindrome(99) == (8, 10)

def test_even_odd_palindrome_includes_101():
    assert even_odd_palindrome(101) == (8, 11)

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
    (12, (4, 6))
])
def test_even_odd_palindrome_parametrized(n, expected):
    assert even_odd_palindrome(n) == expected

def test_even_odd_palindrome_medium_range():
    assert even_odd_palindrome(50) == (6, 7)

def test_even_odd_palindrome_includes_palindromes_up_to_77():
    assert even_odd_palindrome(77) == (7, 9)

def test_even_odd_palindrome_boundary_cases():
    assert even_odd_palindrome(121) == (8, 13)