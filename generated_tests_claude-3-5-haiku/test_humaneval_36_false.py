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
from typing import List

def fizz_buzz(n: int):
    if not isinstance(n, int) or n < 0:
        raise TypeError("Input must be a non-negative integer")
    
    ns = []
    for i in range(1, n+1):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans

def test_fizz_buzz_zero():
    assert fizz_buzz(0) == 0

def test_fizz_buzz_small_numbers():
    assert fizz_buzz(10) == 0
    assert fizz_buzz(15) == 1

def test_fizz_buzz_larger_numbers():
    assert fizz_buzz(50) == 3
    assert fizz_buzz(100) == 6

@pytest.mark.parametrize("input_n,expected", [
    (0, 0),
    (10, 0),
    (15, 1),
    (50, 3),
    (100, 6),
    (200, 12)
])
def test_fizz_buzz_parametrized(input_n, expected):
    assert fizz_buzz(input_n) == expected

def test_fizz_buzz_type_error():
    with pytest.raises(TypeError):
        fizz_buzz("not an integer")

def test_fizz_buzz_negative_input():
    with pytest.raises(TypeError):
        fizz_buzz(-5)