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

def test_get_odd_collatz_even_input():
    assert get_odd_collatz(2) == []
    assert get_odd_collatz(4) == []
    assert get_odd_collatz(6) == [3, 5]

def test_get_odd_collatz_odd_input():
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(3) == [3, 10, 5, 16, 8, 4, 2]
    assert get_odd_collatz(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2]

def test_get_odd_collatz_zero_input():
    with pytest.raises(ValueError):
        get_odd_collatz(0)

@pytest.mark.parametrize("input,expected", [
    (-1, ValueError),
    (-10, ValueError),
    (float(1.5), ValueError)
])
def test_get_odd_collatz_invalid_input(input, expected):
    with pytest.raises(expected):
        get_odd_collatz(input)

def get_odd_collatz(n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError("Input must be a positive integer")
    if n % 2 == 0:
        odd_collatz = [] 
    else:
        odd_collatz = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        if n % 2 == 1:
            odd_collatz.append(int(n))
    return sorted(odd_collatz)