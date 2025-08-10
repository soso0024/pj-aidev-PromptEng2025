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
    for i, x in enumerate(lst):
        if i % 3 == 0:
            result.append(x**2)
        elif i % 4 == 0 and i % 3 != 0:
            result.append(x**3)
        else:
            result.append(x)
    return sum(result)

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_single_element():
    assert sum_squares([5]) == 25

def test_sum_squares_multiple_elements():
    assert sum_squares([2, 3, 4, 5, 6, 7]) == 4 + 9 + 16 + 25 + 36 + 7

def test_sum_squares_all_divisible_by_three():
    assert sum_squares([3, 6, 9, 12, 15]) == 9 + 36 + 81 + 144 + 225

def test_sum_squares_all_divisible_by_four():
    assert sum_squares([4, 8, 12, 16, 20]) == 16 + 512 + 144 + 256 + 400

def test_sum_squares_mixed_divisibility():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1 + 4 + 27 + 16 + 5 + 36 + 7 + 64 + 81 + 100

def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -2, -3, -4, -5]) == 1 + 4 + 27 + 16 + 25

@pytest.mark.parametrize("input,expected", [
    ([1, 'a', 3], TypeError),
    ([1, 2, None], TypeError),
    (None, TypeError)
])
def test_sum_squares_invalid_input(input, expected):
    with pytest.raises(expected):
        sum_squares(input)