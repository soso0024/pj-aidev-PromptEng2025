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

def get_odd_collatz(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    odd_collatz = [n] if n % 2 == 1 else []
    
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        
        if n % 2 == 1:
            odd_collatz.append(int(n))
    
    return sorted(odd_collatz)

def test_get_odd_collatz_odd_input():
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]

def test_get_odd_collatz_even_input():
    assert get_odd_collatz(8) == [1]

def test_get_odd_collatz_one():
    assert get_odd_collatz(1) == [1]

def test_get_odd_collatz_large_number():
    result = get_odd_collatz(27)
    assert len(result) > 0
    assert all(x % 2 == 1 for x in result)

def test_get_odd_collatz_negative_input():
    with pytest.raises(ValueError):
        get_odd_collatz(-5)

@pytest.mark.parametrize("input_num,expected", [
    (7, [1, 5, 7, 11, 13, 17]),
    (1, [1]),
    (3, [1, 3, 5]),
    (15, [1, 5, 13, 15, 23, 35, 41, 53])
])
def test_get_odd_collatz_parametrized(input_num, expected):
    assert get_odd_collatz(input_num) == expected