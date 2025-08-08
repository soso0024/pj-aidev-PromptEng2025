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

def fizz_buzz(n: int):
    if n < 0 or not isinstance(n, int):
        raise ValueError("Input must be a non-negative integer")

    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(map(str, ns))
    return sum(c == '7' for c in s)

@pytest.mark.parametrize("input,expected", [
    (50, 0),
    (78, 2),
    (79, 3),
    (0, 0),
    (11, 0),
    (13, 0),
    (22, 0),
    (33, 0),
    (44, 0),
    (55, 0),
    (66, 0),
    (77, 1),
    (88, 1),
    (99, 1)
])
def test_fizz_buzz(input, expected):
    assert fizz_buzz(input) == expected

def test_fizz_buzz_negative_input():
    with pytest.raises(ValueError):
        fizz_buzz(-1)

def test_fizz_buzz_float_input():
    with pytest.raises(ValueError):
        fizz_buzz(3.14)

def test_fizz_buzz_string_input():
    with pytest.raises(ValueError):
        fizz_buzz("42")