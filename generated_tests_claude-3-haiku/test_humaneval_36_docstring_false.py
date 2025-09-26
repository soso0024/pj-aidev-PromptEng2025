# Test cases for HumanEval/36
# Generated using Claude API



def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans


# Generated test cases:
import pytest
from collections import Counter

@pytest.mark.parametrize("n,expected", [
    (50, 0),
    (78, 2),
    (79, 3),
    (0, 0),
    (11, 0),
    (13, 1),
    (22, 0),
    (77, 2),
    (100, 3),
    (-10, 0),
    (10.0, TypeError),
    ('10', TypeError)
])
def test_fizz_buzz(n, expected):
    if isinstance(n, (float, str)):
        with pytest.raises(expected):
            fizz_buzz(n)
    else:
        result = fizz_buzz(n)
        assert result == expected

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    ns = [i for i in range(n) if i % 11 == 0 or i % 13 == 0]
    s = ''.join(map(str, ns))
    return s.count('7')