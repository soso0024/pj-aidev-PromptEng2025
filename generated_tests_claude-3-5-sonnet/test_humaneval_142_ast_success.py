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

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], 147),  # 1^2 + 2 + 9 + 64 + 5
    ([0, 0, 0, 0, 0], 0),
    ([1, 1, 1, 1, 1], 5),  # 1^2 + 1 + 1 + 1 + 1
    ([2, 2, 2, 2, 2], 20),  # 4 + 2 + 4 + 8 + 2
])
def test_various_lists(input_list, expected):
    assert sum_squares(input_list) == expected

@pytest.mark.parametrize("input_list,expected", [
    ([-1, -2, -3], -4),  # 1 + (-2) + 9
    ([-2, -2, -2, -2], 4),  # 4 + (-2) + 4 + (-8)
])
def test_negative_numbers(input_list, expected):
    assert sum_squares(input_list) == expected

def test_large_numbers():
    assert sum_squares([100, 200, 300]) == 10500  # 10000 + 200 + 300

@pytest.mark.parametrize("input_list", [
    [1.5, 2.5, 3.5],
    [0.1, 0.2, 0.3],
])
def test_float_numbers(input_list):
    result = sum_squares(input_list)
    assert isinstance(result, float)

@pytest.mark.parametrize("invalid_input", [
    None,
    42,
    "string",
    True
])
def test_invalid_input_type(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        sum_squares(invalid_input)

def test_large_list():
    large_list = list(range(1000))
    result = sum_squares(large_list)
    assert isinstance(result, (int, float))
    assert result > 0

def test_alternating_positive_negative():
    assert sum_squares([1, -1, 2, -2, 3]) == 33  # 1 + (-1) + 4 + (-2) + 9

def test_list_with_zeros():
    assert sum_squares([0, 1, 0, 2, 0]) == 5  # 0 + 1 + 0 + 8 + 0