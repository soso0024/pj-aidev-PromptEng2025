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

def test_fizz_buzz_small():
    assert fizz_buzz(15) == 0

def test_fizz_buzz_with_sevens():
    assert fizz_buzz(78) == 2

def test_fizz_buzz_large():
    assert fizz_buzz(100) == 3

@pytest.mark.parametrize("input_n,expected", [
    (11, 0),
    (13, 0),
    (22, 0),
    (26, 0),
    (77, 0),
    (87, 3),
    (170, 4),
    (1000, 47)
])
def test_fizz_buzz_various_inputs(input_n, expected):
    assert fizz_buzz(input_n) == expected

def test_fizz_buzz_negative():
    assert fizz_buzz(-5) == 0

@pytest.mark.parametrize("input_n", [
    None,
    "string",
    3.14,
    [],
    {}
])
def test_fizz_buzz_invalid_inputs(input_n):
    with pytest.raises((TypeError, AttributeError)):
        fizz_buzz(input_n)

def test_fizz_buzz_large_number():
    assert fizz_buzz(10000) == 639

def test_fizz_buzz_consecutive_sevens():
    assert fizz_buzz(78) == 2

def test_fizz_buzz_boundary():
    assert fizz_buzz(1) == 0
    assert fizz_buzz(2) == 0