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
    (["((", "("], "No"),
    ([")", "("], "No"),
    (["(())", "()"], "Yes"),
    (["((())", ")"], "Yes"),
    (["", ""], "Yes"),
    (["(", ""], "No"),
    (["((())", ")))"], "No"),
    (["(((", ")))"], "Yes"),
    ([")(", ")("], "No"),
    (["(())", "(())"], "Yes"),
    (["(()", "())"], "Yes")
])
def test_match_parens(input_lst, expected):
    assert match_parens(input_lst) == expected

def test_match_parens_empty_list():
    with pytest.raises(IndexError):
        match_parens([])

def test_match_parens_single_element():
    with pytest.raises(IndexError):
        match_parens(["("])

def test_match_parens_too_many_elements():
    with pytest.raises(IndexError):
        match_parens(["(", ")", "("])

def test_match_parens_invalid_input_type():
    with pytest.raises(TypeError):
        match_parens(None)
    with pytest.raises(TypeError):
        match_parens("()")
    with pytest.raises(TypeError):
        match_parens(123)

def test_match_parens_invalid_characters():
    with pytest.raises(ValueError):
        match_parens(["a()", ")"])
    with pytest.raises(ValueError):
        match_parens(["()", "123"])

def match_parens(lst):
    if lst is None or not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) != 2:
        raise IndexError("List must contain exactly 2 elements")
    if not all(isinstance(s, str) for s in lst):
        raise TypeError("List elements must be strings")
    if not all(all(c in '()' for c in s) for s in lst):
        raise ValueError("Strings can only contain parentheses")
        
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

    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]
    return 'Yes' if check(S1) or check(S2) else 'No'