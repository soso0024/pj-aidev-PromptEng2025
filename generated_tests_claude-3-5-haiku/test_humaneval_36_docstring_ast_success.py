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
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")

    ns = []
    for i in range(n):
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
    assert fizz_buzz(15) == 0

def test_fizz_buzz_known_cases():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3

def test_fizz_buzz_larger_numbers():
    assert fizz_buzz(100) == 3
    assert fizz_buzz(200) == 6

@pytest.mark.parametrize("input,expected", [
    (0, 0),
    (10, 0),
    (50, 0),
    (78, 2),
    (79, 3),
    (100, 3),
    (200, 6)
])
def test_fizz_buzz_parametrized(input, expected):
    assert fizz_buzz(input) == expected

def test_fizz_buzz_type_error():
    with pytest.raises(TypeError):
        fizz_buzz("not an integer")
    with pytest.raises(TypeError):
        fizz_buzz(3.14)

def test_fizz_buzz_negative_input():
    with pytest.raises(ValueError):
        fizz_buzz(-1)