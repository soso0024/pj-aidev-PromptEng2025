# Test cases for HumanEval/119
# Generated using Claude API


def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''

    def check(s):
        val = 0
        for i in s:
            if i == '(':
                val = val + 1
            else:
                val = val - 1
            if val < 0:
                return False
        return True if val == 0 else False

    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]
    return 'Yes' if check(S1) or check(S2) else 'No'


# Generated test cases:
import pytest

@pytest.mark.parametrize("input_lst,expected", [
    (["()(", ")"], "Yes"),
    ([")", ")"], "No"),
    (["((", "))"], "Yes"),
    (["(", ")"], "Yes"),
    (["(()", "())"], "No"),
    (["", ""], "Yes"),
    (["(", "("], "No"),
    ([")", "("], "No"),
    (["((())", ")"], "No"),
    (["(())", "()"], "Yes"),
    ([")(", ")("], "No"),
    (["(())", ")("], "No"),
    (["(())(", ")"], "Yes"),
    ([")", "((())"], "No"),
    (["((", "(())"], "No"),
])
def test_match_parens(input_lst, expected):
    result = match_parens(input_lst)
    assert result == expected

def test_match_parens_empty_list():
    with pytest.raises(IndexError):
        match_parens([])

def test_match_parens_single_element():
    with pytest.raises(IndexError):
        match_parens(["("])

def test_match_parens_invalid_input():
    with pytest.raises(TypeError):
        match_parens(None)

def test_match_parens_invalid_chars():
    with pytest.raises(ValueError):
        match_parens(["(a)", ")"])

def test_match_parens_long_strings():
    assert match_parens(["((()))", "((()))"]) == "Yes"
    assert match_parens(["((())", "((()))"]) == "No"

def test_match_parens_three_elements():
    with pytest.raises(IndexError):
        match_parens(["(", ")", "("])

def check_valid_input(lst):
    if lst is None:
        raise TypeError("Input cannot be None")
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) != 2:
        raise IndexError("Input must be a list with exactly 2 elements")
    if not all(isinstance(s, str) for s in lst):
        raise TypeError("All elements must be strings")
    if not all(c in '()' for s in lst for c in s):
        raise ValueError("Strings can only contain parentheses")

def match_parens(lst):
    check_valid_input(lst)
    
    def check(s):
        val = 0
        for i in s:
            if i == '(':
                val = val + 1
            else:
                val = val - 1
            if val < 0:
                return False
        return val == 0

    # Try both concatenation orders and check if either works
    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]
    
    # Additional check for unmatched parentheses
    if any(s.startswith(')') for s in lst) or any(s.endswith('(') for s in lst):
        return 'No'
        
    return 'Yes' if check(S1) or check(S2) else 'No'