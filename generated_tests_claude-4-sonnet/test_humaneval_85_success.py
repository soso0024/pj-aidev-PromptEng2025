# Test cases for HumanEval/85
# Generated using Claude API


def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])


# Generated test cases:
import pytest

def add(lst):
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])

class TestAdd:
    
    def test_empty_list(self):
        assert add([]) == 0
    
    def test_single_element(self):
        assert add([1]) == 0
    
    def test_two_elements_odd_at_index_1(self):
        assert add([1, 3]) == 0
    
    def test_two_elements_even_at_index_1(self):
        assert add([1, 4]) == 4
    
    def test_three_elements_odd_at_index_1(self):
        assert add([1, 3, 5]) == 0
    
    def test_three_elements_even_at_index_1(self):
        assert add([1, 2, 5]) == 2
    
    def test_four_elements_both_odd_at_odd_indices(self):
        assert add([1, 3, 5, 7]) == 0
    
    def test_four_elements_both_even_at_odd_indices(self):
        assert add([1, 2, 5, 4]) == 6
    
    def test_four_elements_mixed_at_odd_indices(self):
        assert add([1, 2, 5, 7]) == 2
    
    def test_four_elements_mixed_at_odd_indices_reverse(self):
        assert add([1, 3, 5, 6]) == 6
    
    def test_longer_list_all_even_at_odd_indices(self):
        assert add([1, 2, 3, 4, 5, 6, 7, 8]) == 20
    
    def test_longer_list_all_odd_at_odd_indices(self):
        assert add([1, 1, 3, 3, 5, 5, 7, 7]) == 0
    
    def test_longer_list_mixed_at_odd_indices(self):
        assert add([0, 2, 1, 3, 2, 4, 3, 5]) == 6
    
    def test_negative_numbers_even(self):
        assert add([1, -2, 3, -4]) == -6
    
    def test_negative_numbers_odd(self):
        assert add([1, -1, 3, -3]) == 0
    
    def test_zero_at_odd_index(self):
        assert add([1, 0, 3, 4]) == 4
    
    def test_all_zeros(self):
        assert add([0, 0, 0, 0]) == 0
    
    @pytest.mark.parametrize("input_list,expected", [
        ([1, 2], 2),
        ([1, 3], 0),
        ([5, 6, 7, 8], 14),
        ([1, 1, 1, 1, 1, 1], 0),
        ([2, 4, 6, 8, 10, 12], 24),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 30)
    ])
    def test_parametrized_cases(self, input_list, expected):
        assert add(input_list) == expected