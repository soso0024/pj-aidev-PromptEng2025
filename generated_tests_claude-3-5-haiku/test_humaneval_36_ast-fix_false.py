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

def test_fizz_buzz_zero():
    assert fizz_buzz(0) == 0

def test_fizz_buzz_small():
    assert fizz_buzz(50) == 0

def test_fizz_buzz_medium():
    assert fizz_buzz(78) == 2

def test_fizz_buzz_large():
    assert fizz_buzz(79) == 3

def test_fizz_buzz_negative():
    with pytest.raises(ValueError):
        fizz_buzz(-1)