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

def test_empty_list():
    assert sum_squares([]) == 0

def test_single_element():
    assert sum_squares([5]) == 25

def test_two_elements():
    assert sum_squares([2, 3]) == 7

def test_three_elements():
    assert sum_squares([1, 2, 3]) == 6

def test_four_elements():
    assert sum_squares([2, 3, 4, 5]) == 36

def test_five_elements():
    assert sum_squares([1, 2, 3, 4, 5]) == 147

@pytest.mark.parametrize("lst,expected", [
    ([1], 1),
    ([2, 3], 7),
    ([1, 2, 3], 6),
    ([2, 3, 4, 5], 36),
    ([1, 2, 3, 4, 5], 147),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 717),
    ([10], 100),
    ([-1, -2, -3], -4),
    ([-2, -3, -4, -5], 22),
])
def test_parametrized_cases(lst, expected):
    assert sum_squares(lst) == expected

def test_negative_numbers():
    assert sum_squares([-1, -2, -3, -4]) == 12

def test_zeros():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_mixed_positive_negative():
    assert sum_squares([1, -2, 3, -4]) == 18

def test_large_numbers():
    assert sum_squares([100, 200, 300]) == 10500

def test_index_multiples():
    assert sum_squares([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 13

def test_index_zero_only():
    assert sum_squares([3]) == 9

def test_index_four_only():
    assert sum_squares([0, 0, 0, 0, 2]) == 8

def test_index_twelve():
    lst = [0] * 13
    lst[12] = 2
    assert sum_squares(lst) == 4

def test_floating_point():
    assert sum_squares([2.5]) == 6.25

def test_floating_point_complex():
    result = sum_squares([1.5, 2.5, 3.5])
    expected = 1.5**2 + 2.5 + 3.5
    assert abs(result - expected) < 1e-10