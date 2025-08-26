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

def test_fizz_buzz_small_numbers():
    assert fizz_buzz(10) == 0
    assert fizz_buzz(15) == 0

def test_fizz_buzz_known_cases():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3

@pytest.mark.parametrize("input,expected", [
    (0, 0),
    (10, 0),
    (50, 0),
    (78, 2),
    (79, 3),
    (100, 4),
    (200, 8)
])
def test_fizz_buzz_parametrized(input, expected):
    assert fizz_buzz(input) == expected

def test_fizz_buzz_large_number():
    assert fizz_buzz(1000) > 0

def test_fizz_buzz_type_error():
    with pytest.raises(TypeError):
        fizz_buzz("not an integer")

def test_fizz_buzz_negative_input():
    with pytest.raises(ValueError):
        fizz_buzz(-1)