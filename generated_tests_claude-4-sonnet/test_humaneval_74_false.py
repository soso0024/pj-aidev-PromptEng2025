# Test cases for HumanEval/74
# Generated using Claude API


def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''

    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2


# Generated test cases:
import pytest

def total_match(lst1, lst2):
    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2

class TestTotalMatch:
    
    def test_empty_lists(self):
        assert total_match([], []) == []
    
    def test_first_list_empty(self):
        assert total_match([], ["hello", "world"]) == []
    
    def test_second_list_empty(self):
        assert total_match(["hello", "world"], []) == ["hello", "world"]
    
    def test_equal_total_length_returns_first(self):
        assert total_match(["hi", "bye"], ["test"]) == ["hi", "bye"]
    
    def test_first_list_shorter_total(self):
        assert total_match(["a", "b"], ["hello", "world"]) == ["a", "b"]
    
    def test_second_list_shorter_total(self):
        assert total_match(["hello", "world"], ["a", "b"]) == ["a", "b"]
    
    def test_single_element_lists(self):
        assert total_match(["short"], ["verylongstring"]) == ["short"]
    
    def test_single_element_equal_length(self):
        assert total_match(["hello"], ["world"]) == ["hello"]
    
    def test_multiple_empty_strings(self):
        assert total_match(["", "", ""], ["", ""]) == ["", ""]
    
    def test_mixed_empty_and_non_empty_strings(self):
        assert total_match(["", "hello", ""], ["world"]) == ["world"]
    
    @pytest.mark.parametrize("lst1,lst2,expected", [
        (["a"], ["bb"], ["a"]),
        (["aa"], ["b"], ["b"]),
        (["abc", "def"], ["ghijkl"], ["abc", "def"]),
        (["x", "y", "z"], ["abc"], ["x", "y", "z"]),
        (["python"], ["java", "c++"], ["java", "c++"]),
    ])
    def test_parametrized_cases(self, lst1, lst2, expected):
        assert total_match(lst1, lst2) == expected
    
    def test_very_long_strings(self):
        long_string = "a" * 1000
        short_strings = ["b"] * 999
        assert total_match([long_string], short_strings) == short_strings
    
    def test_many_short_vs_few_long(self):
        many_short = ["a"] * 100
        few_long = ["b" * 50, "c" * 50]
        assert total_match(many_short, few_long) == many_short
    
    def test_identical_lists(self):
        lst = ["hello", "world", "test"]
        assert total_match(lst, lst) == lst
    
    def test_single_character_strings(self):
        assert total_match(["a", "b", "c"], ["x", "y"]) == ["x", "y"]