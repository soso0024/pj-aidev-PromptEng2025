# Test cases for HumanEval/94
# Generated using Claude API



def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """

    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False

        return True
    maxx = 0
    i = 0
    while i < len(lst):
        if(lst[i] > maxx and isPrime(lst[i])):
            maxx = lst[i]
        i+=1
    result = sum(int(digit) for digit in str(maxx))
    return result



# Generated test cases:
import pytest

def skjkasdkd(lst):
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    maxx = 0
    i = 0
    while i < len(lst):
        if(lst[i] > maxx and isPrime(lst[i])):
            maxx = lst[i]
        i+=1
    result = sum(int(digit) for digit in str(maxx))
    return result

@pytest.mark.parametrize("lst,expected", [
    ([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3], 10),
    ([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1], 25),
    ([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3], 13),
    ([0,724,32,71,99,32,6,0,5,91,83,0,5,6], 11),
    ([0,81,12,3,1,21], 3),
    ([0,8,1,2,1,7], 7)
])
def test_skjkasdkd_examples(lst, expected):
    assert skjkasdkd(lst) == expected

def test_skjkasdkd_empty_list():
    assert skjkasdkd([]) == 0

def test_skjkasdkd_no_primes():
    assert skjkasdkd([0, 1, 4, 6, 8, 9, 10, 12]) == 0

def test_skjkasdkd_single_prime():
    assert skjkasdkd([2]) == 2
    assert skjkasdkd([3]) == 3
    assert skjkasdkd([5]) == 5
    assert skjkasdkd([7]) == 7

def test_skjkasdkd_single_non_prime():
    assert skjkasdkd([1]) == 0
    assert skjkasdkd([4]) == 0
    assert skjkasdkd([0]) == 0

def test_skjkasdkd_large_primes():
    assert skjkasdkd([97]) == 16
    assert skjkasdkd([101]) == 2
    assert skjkasdkd([997]) == 25

def test_skjkasdkd_mixed_with_negatives():
    assert skjkasdkd([-5, -3, 2, 3, 5]) == 5

def test_skjkasdkd_duplicates():
    assert skjkasdkd([2, 2, 2, 2]) == 2
    assert skjkasdkd([3, 5, 3, 5, 7, 7]) == 7

def test_skjkasdkd_large_numbers():
    assert skjkasdkd([1009]) == 10
    assert skjkasdkd([1013]) == 5

def test_skjkasdkd_zero_and_one():
    assert skjkasdkd([0, 1]) == 0

def test_skjkasdkd_small_primes():
    assert skjkasdkd([2, 3, 5, 7, 11, 13]) == 4