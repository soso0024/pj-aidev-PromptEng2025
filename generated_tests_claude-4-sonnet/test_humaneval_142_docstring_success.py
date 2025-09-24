# Test cases for HumanEval/142
# Generated using Claude API




def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """

    result =[]
    for i in range(len(lst)):
        if i %3 == 0:
            result.append(lst[i]**2)
        elif i % 4 == 0 and i%3 != 0:
            result.append(lst[i]**3)
        else:
            result.append(lst[i])
    return sum(result)


# Generated test cases:
import pytest

def sum_squares(lst):
    result =[]
    for i in range(len(lst)):
        if i %3 == 0:
            result.append(lst[i]**2)
        elif i % 4 == 0 and i%3 != 0:
            result.append(lst[i]**3)
        else:
            result.append(lst[i])
    return sum(result)

@pytest.mark.parametrize("lst,expected", [
    ([1, 2, 3], 6),
    ([], 0),
    ([-1, -5, 2, -1, -5], -126),
    ([0], 0),
    ([1], 1),
    ([1, 2], 3),
    ([1, 2, 3, 4], 22),
    ([1, 2, 3, 4, 5], 147),
    ([1, 2, 3, 4, 5, 6], 153),
    ([1, 2, 3, 4, 5, 6, 7], 202),
    ([1, 2, 3, 4, 5, 6, 7, 8], 210),
    ([0, 0, 0, 0], 0),
    ([-1, -2, -3, -4], 12),
    ([2, 3, 4, 5, 6, 7, 8, 9], 332),
    ([10], 100),
    ([10, 20], 120),
    ([10, 20, 30], 150),
    ([10, 20, 30, 40], 1750),
    ([-5, -4, -3, -2, -1], 21),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 12),
])
def test_sum_squares(lst, expected):
    assert sum_squares(lst) == expected

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_single_element():
    assert sum_squares([5]) == 25

def test_sum_squares_negative_numbers():
    assert sum_squares([-2, -3, -4]) == -3

def test_sum_squares_zeros():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_sum_squares_large_numbers():
    assert sum_squares([100, 200, 300]) == 10500

def test_sum_squares_index_multiples():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    expected = 1**2 + 2 + 3**2 + 4**3 + 5 + 6**2 + 7 + 8**3 + 9**2 + 10 + 11 + 12**2
    assert sum_squares(lst) == 1062