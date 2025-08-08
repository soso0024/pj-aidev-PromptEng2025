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

def test_get_odd_collatz_empty():
    assert get_odd_collatz(1) == [1]

def test_get_odd_collatz_single_odd():
    assert get_odd_collatz(5) == [1, 5]

def test_get_odd_collatz_multiple_odds():
    assert get_odd_collatz(7) == [1, 7, 21]

def test_get_odd_collatz_even():
    assert get_odd_collatz(6) == []

@pytest.mark.parametrize("input,expected", [
    (0, []),
    (-5, []),
    (3.14, []),
    ('test', [])
])
def test_get_odd_collatz_invalid_input(input, expected):
    assert get_odd_collatz(input) == expected

def get_odd_collatz(n):
    if isinstance(n, int) and n > 0:
        odd_collatz = [] if n % 2 == 0 else [n]
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            if n % 2 == 1:
                odd_collatz.append(int(n))
        return sorted(odd_collatz)
    else:
        return []