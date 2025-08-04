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
    assert sum_squares([2]) == 4

def test_sum_squares_basic_list():
    assert sum_squares([1, 2, 3, 4, 5]) == 147

def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -2, -3, -4, -5]) == -113

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5, 6], 153),
    ([0, 0, 0, 0, 0], 0),
    ([10, 20, 30, 40, 50], 126750),
    ([-2, -1, 0, 1, 2], 12),
    ([1.5, 2.5, 3.5, 4.5, 5.5], 194.875)
])
def test_sum_squares_parametrized(input_list, expected):
    assert sum_squares(input_list) == expected

def test_sum_squares_large_numbers():
    assert sum_squares([100, 200, 300, 400, 500]) == 125170500

def test_sum_squares_mixed_numbers():
    assert sum_squares([-1, 0, 1, -2, 2]) == 14

def test_sum_squares_zeros():
    assert sum_squares([0, 0, 0]) == 0

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    3.14,
    [1, "2", 3],
    [[], 2, 3],
    [{1: 2}, 2, 3]
])
def test_sum_squares_invalid_input(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        if isinstance(invalid_input, list):
            sum_squares(invalid_input)
        else:
            sum_squares(invalid_input)

def test_sum_squares_long_list():
    input_list = list(range(100))
    assert sum_squares(input_list) > 0

def test_sum_squares_floating_point():
    result = sum_squares([1.1, 2.2, 3.3, 4.4, 5.5])
    assert abs(result - 192.445) < 0.0001