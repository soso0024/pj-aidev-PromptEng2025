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

def test_fizz_buzz_small_number():
    assert fizz_buzz(10) == 0

def test_fizz_buzz_with_sevens():
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3

def test_fizz_buzz_large_number():
    assert fizz_buzz(100) == 3

@pytest.mark.parametrize("input_n,expected", [
    (50, 0),
    (78, 2),
    (79, 3),
    (80, 3),
    (200, 6)
])
def test_fizz_buzz_parametrized(input_n, expected):
    assert fizz_buzz(input_n) == expected

def test_fizz_buzz_specific_numbers():
    assert fizz_buzz(11) == 0  # Just includes number 0
    assert fizz_buzz(14) == 0  # Includes 0, 11, 13
    assert fizz_buzz(78) == 2  # Includes numbers with 7

@pytest.mark.parametrize("invalid_input", [
    -1,
    -100,
    -1000
])
def test_fizz_buzz_negative_numbers(invalid_input):
    assert fizz_buzz(invalid_input) == 0

def test_fizz_buzz_edge_cases():
    assert fizz_buzz(1) == 0
    assert fizz_buzz(7) == 0
    assert fizz_buzz(77777) > 0

def test_fizz_buzz_consecutive_sevens():
    assert fizz_buzz(78) == 2
    assert fizz_buzz(177) > fizz_buzz(77)