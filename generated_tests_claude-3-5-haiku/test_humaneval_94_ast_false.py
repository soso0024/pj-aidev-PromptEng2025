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
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    if not lst:
        return 0
    
    maxx = 0
    for num in lst:
        if num > maxx and isPrime(num):
            maxx = num
    
    if maxx == 0:
        return 0
    
    result = sum(int(digit) for digit in str(maxx))
    return result

def test_skjkasdkd_normal_case():
    assert skjkasdkd([3, 4, 5, 6, 7]) == 7
    assert skjkasdkd([1, 2, 3, 4, 5]) == 2
    assert skjkasdkd([10, 11, 12, 13, 14]) == 4

def test_skjkasdkd_prime_numbers():
    assert skjkasdkd([2, 3, 5, 7, 11]) == 2
    assert skjkasdkd([17, 19, 23, 29]) == 20

def test_skjkasdkd_large_numbers():
    assert skjkasdkd([100, 101, 103, 107]) == 1
    assert skjkasdkd([997, 1009, 1013]) == 28

def test_skjkasdkd_edge_cases():
    assert skjkasdkd([]) == 0
    assert skjkasdkd([1]) == 0
    assert skjkasdkd([4, 6, 8, 10]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([3, 4, 5, 6, 7], 7),
    ([1, 2, 3, 4, 5], 2),
    ([10, 11, 12, 13, 14], 4),
    ([2, 3, 5, 7, 11], 2),
    ([100, 101, 103, 107], 1),
    ([], 0),
    ([1], 0)
])
def test_skjkasdkd_parametrized(input_list, expected):
    assert skjkasdkd(input_list) == expected

def test_skjkasdkd_type_error():
    with pytest.raises(TypeError):
        skjkasdkd(None)
    with pytest.raises(TypeError):
        skjkasdkd("not a list")