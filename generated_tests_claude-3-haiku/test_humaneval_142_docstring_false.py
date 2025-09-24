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

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_single_element():
    assert sum_squares([5]) == 25

def test_sum_squares_multiple_elements():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_with_zeros():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_sum_squares_with_negative_numbers():
    assert sum_squares([-1, -2, -3, -4]) == -30

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 220),
    ([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], -330),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
])
def test_sum_squares_with_parametrize(input_list, expected):
    assert sum_squares(input_list) == expected

def test_sum_squares_with_non_integer_elements():
    with pytest.raises(TypeError):
        sum_squares([1, 2.5, 3])