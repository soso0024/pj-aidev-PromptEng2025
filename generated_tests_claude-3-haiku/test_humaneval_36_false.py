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

def test_fizz_buzz_zero():
    assert fizz_buzz(0) == 0

def test_fizz_buzz_one():
    assert fizz_buzz(1) == 0

def test_fizz_buzz_eleven():
    assert fizz_buzz(11) == 1

def test_fizz_buzz_thirteen():
    assert fizz_buzz(13) == 1

def test_fizz_buzz_twenty_two():
    assert fizz_buzz(22) == 2

def test_fizz_buzz_negative_value():
    with pytest.raises(ValueError):
        fizz_buzz(-1)

@pytest.mark.parametrize("input,expected", [
    (0, 0),
    (1, 0),
    (11, 1),
    (13, 1),
    (22, 2),
    (-1, ValueError)
])
def test_fizz_buzz_parametrized(input, expected):
    if expected == ValueError:
        with pytest.raises(ValueError):
            fizz_buzz(input)
    else:
        assert fizz_buzz(input) == expected

def fizz_buzz(n: int):
    if n < 0:
        raise ValueError("n must be non-negative")
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans