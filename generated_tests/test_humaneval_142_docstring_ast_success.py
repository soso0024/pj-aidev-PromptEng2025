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

def test_empty_list():
    assert sum_squares([]) == 0

def test_single_element():
    assert sum_squares([1]) == 1

def test_two_elements():
    assert sum_squares([1, 2]) == 3

def test_three_elements():
    assert sum_squares([1, 2, 3]) == 6

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_four_elements():
    assert sum_squares([2, 3, 4, 5]) == 36

@pytest.mark.parametrize("input_list,expected", [
    ([1, 1, 1, 1, 1], 5),
    ([2, 2, 2, 2, 2, 2], 22),
    ([0, 0, 0, 0], 0),
    ([10, -2, 3, 4, 5, 6], 248),
    ([-1, -1, -1, -1], 0)
])
def test_multiple_cases(input_list, expected):
    assert sum_squares(input_list) == expected

def test_large_numbers():
    assert sum_squares([100, 200, 300]) == 10500

def test_zeros_and_ones():
    assert sum_squares([0, 1, 0, 1, 0]) == 2

def test_alternating_signs():
    assert sum_squares([1, -1, 1, -1, 1]) == 3

def test_all_same_number():
    assert sum_squares([5, 5, 5, 5]) == 60

def test_sequence():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 153

def test_long_sequence():
    assert sum_squares(list(range(10))) == 717