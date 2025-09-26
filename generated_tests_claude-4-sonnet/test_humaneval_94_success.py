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

def test_empty_list():
    assert skjkasdkd([]) == 0

def test_no_primes():
    assert skjkasdkd([4, 6, 8, 9, 10, 12]) == 0

def test_single_prime():
    assert skjkasdkd([7]) == 7

def test_single_non_prime():
    assert skjkasdkd([4]) == 0

def test_multiple_primes():
    assert skjkasdkd([2, 3, 5, 7, 11]) == 2

def test_mixed_numbers():
    assert skjkasdkd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7

def test_large_prime():
    assert skjkasdkd([97]) == 16

def test_prime_with_multiple_digits():
    assert skjkasdkd([23, 29, 31]) == 4

def test_duplicates():
    assert skjkasdkd([7, 7, 7]) == 7

def test_one_is_not_prime():
    assert skjkasdkd([1]) == 0

def test_zero_and_negative():
    assert skjkasdkd([0, -5, -7]) == 0

def test_two_is_prime():
    assert skjkasdkd([2]) == 2

def test_large_numbers():
    assert skjkasdkd([101, 103, 107]) == 8

def test_mixed_with_negatives():
    assert skjkasdkd([-5, 2, 3, -7, 11]) == 2

def test_largest_prime_selected():
    assert skjkasdkd([2, 13, 5, 7, 11]) == 4

def test_three_digit_prime():
    assert skjkasdkd([113]) == 5

def test_prime_sum_of_digits():
    assert skjkasdkd([89]) == 17

@pytest.mark.parametrize("lst,expected", [
    ([2, 3, 5], 5),
    ([11, 13, 17], 8),
    ([4, 6, 8], 0),
    ([19, 23, 29], 11),
    ([37, 41, 43], 7)
])
def test_parametrized_cases(lst, expected):
    assert skjkasdkd(lst) == expected