# Test cases for HumanEval/123
# Generated using Claude API


def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """

    if n%2==0:
        odd_collatz = [] 
    else:
        odd_collatz = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
            
        if n%2 == 1:
            odd_collatz.append(int(n))

    return sorted(odd_collatz)


# Generated test cases:
import pytest

def test_get_odd_collatz_basic():
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(4) == [1]

@pytest.mark.parametrize("input_n,expected", [
    (1, [1]),
    (2, [1]),
    (3, [1, 3, 5]),
    (4, [1]),
    (5, [1, 5]),
    (6, [1, 3, 5]),
    (7, [1, 5, 7, 11, 13, 17]),
    (10, [1, 5]),
    (15, [1, 5, 15, 23, 35, 53]),
    (20, [1, 5])
])
def test_get_odd_collatz_parametrized(input_n, expected):
    assert get_odd_collatz(input_n) == expected

def test_get_odd_collatz_large_number():
    result = get_odd_collatz(100)
    assert result[0] == 1
    assert result[1] == 5
    assert len(result) >= 3

@pytest.mark.parametrize("input_n", [-1, 0, -100])
def test_get_odd_collatz_invalid_input(input_n):
    with pytest.raises(ValueError):
        get_odd_collatz(input_n)

def test_get_odd_collatz_result_sorted():
    result = get_odd_collatz(7)
    assert result == sorted(result)

def test_get_odd_collatz_type():
    result = get_odd_collatz(5)
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)

def test_get_odd_collatz_even_start():
    assert get_odd_collatz(8) == [1]

def test_get_odd_collatz_odd_start():
    result = get_odd_collatz(9)
    assert 1 in result
    assert 9 in result
    assert result == sorted(result)

def test_get_odd_collatz_float_input():
    with pytest.raises(TypeError):
        get_odd_collatz(5.5)

def test_get_odd_collatz_string_input():
    with pytest.raises(TypeError):
        get_odd_collatz("5")