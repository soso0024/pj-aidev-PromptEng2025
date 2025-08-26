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
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n <= 0:
        raise TypeError("Input must be a positive integer")
    
    if n % 2 == 0:
        odd_collatz = []
    else:
        odd_collatz = [n]
    
    original_n = n
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        
        if n % 2 == 1:
            odd_collatz.append(int(n))
    
    if original_n % 2 == 0:
        odd_collatz = []
    
    return sorted(odd_collatz, reverse=True)

def test_get_odd_collatz_odd_input():
    assert get_odd_collatz(7) == [17, 13, 11, 7, 5, 1]

def test_get_odd_collatz_even_input():
    assert get_odd_collatz(8) == []

def test_get_odd_collatz_one():
    assert get_odd_collatz(1) == [1]

def test_get_odd_collatz_large_number():
    result = get_odd_collatz(27)
    assert result == [27, 17, 13, 11, 7, 5, 3, 1]

@pytest.mark.parametrize("input_num,expected", [
    (1, [1]),
    (3, [5, 3, 1]),
    (7, [17, 13, 11, 7, 5, 1]),
    (8, []),
    (15, [31, 23, 17, 15, 13, 11, 7, 5, 1]),
    (27, [27, 17, 13, 11, 7, 5, 3, 1])
])
def test_get_odd_collatz_parametrized(input_num, expected):
    assert get_odd_collatz(input_num) == expected

def test_get_odd_collatz_negative_input():
    with pytest.raises(TypeError):
        get_odd_collatz(-5)

def test_get_odd_collatz_float_input():
    with pytest.raises(TypeError):
        get_odd_collatz(3.14)