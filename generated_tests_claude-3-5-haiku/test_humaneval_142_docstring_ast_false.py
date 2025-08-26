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
    result = []
    for i in range(len(lst)):
        if i % 3 == 0:
            result.append(lst[i]**2)
        elif i % 4 == 0 and i % 3 != 0:
            result.append(lst[i]**3)
        else:
            result.append(lst[i])
    return sum(result)

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_single_element():
    assert sum_squares([5]) == 25

def test_sum_squares_multiple_elements():
    assert sum_squares([1, 2, 3, 4, 5]) == 35

def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], 6),
    ([0, 1, 2, 3, 4], 16),
    ([-2, -3, -4, -5], 16),
    ([10, 20, 30, 40], 2600)
])
def test_sum_squares_parametrized(input_list, expected):
    assert sum_squares(input_list) == expected

def test_sum_squares_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 220000

def test_sum_squares_zero_values():
    assert sum_squares([0, 0, 0, 0, 0]) == 0