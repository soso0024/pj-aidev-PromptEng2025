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
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans

def test_fizz_buzz_docstring_examples():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3

def test_fizz_buzz_edge_cases():
    assert fizz_buzz(0) == 0
    assert fizz_buzz(1) == 0
    assert fizz_buzz(11) == 0
    assert fizz_buzz(12) == 0
    assert fizz_buzz(13) == 0
    assert fizz_buzz(14) == 0

def test_fizz_buzz_small_values():
    assert fizz_buzz(22) == 0
    assert fizz_buzz(26) == 0
    assert fizz_buzz(39) == 0

def test_fizz_buzz_with_sevens():
    assert fizz_buzz(70) == 0
    assert fizz_buzz(71) == 0
    assert fizz_buzz(77) == 0
    assert fizz_buzz(78) == 2

def test_fizz_buzz_larger_values():
    assert fizz_buzz(100) == 3
    assert fizz_buzz(150) == 4
    assert fizz_buzz(200) == 6

@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 0),
    (11, 0),
    (22, 0),
    (50, 0),
    (70, 0),
    (77, 0),
    (78, 2),
    (79, 3),
    (88, 3),
    (100, 3)
])
def test_fizz_buzz_parametrized(n, expected):
    assert fizz_buzz(n) == expected

def test_fizz_buzz_multiples_of_11():
    assert fizz_buzz(67) == 0
    assert fizz_buzz(68) == 0

def test_fizz_buzz_multiples_of_13():
    assert fizz_buzz(79) == 3
    assert fizz_buzz(80) == 3

def test_fizz_buzz_multiples_of_both_11_and_13():
    assert fizz_buzz(144) == 4
    assert fizz_buzz(145) == 4

def test_fizz_buzz_negative_input():
    assert fizz_buzz(-1) == 0

def test_fizz_buzz_type_error():
    with pytest.raises(TypeError):
        fizz_buzz("string")
    with pytest.raises(TypeError):
        fizz_buzz(None)
    with pytest.raises(TypeError):
        fizz_buzz(1.5)