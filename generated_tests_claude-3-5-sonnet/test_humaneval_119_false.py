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
    (["(", ")"], "Yes"),
    ([")", "("], "Yes"),
    (["((", "))"], "Yes"),
    (["()", "()"], "Yes"),
    ([")(", ")("], "No"),
    (["(", "("], "No"),
    ([")", ")"], "No"),
    (["(()", "())"], "Yes"),
    (["())", "(()"], "Yes"),
    (["(())", "()"], "Yes"),
    (["((((", "))))"], "Yes"),
    (["", ""], "Yes"),
    (["(", ""], "No"),
    (["((())", ")"], "Yes"),
    (["(())", "(())"], "Yes"),
    ([")()", "())"], "No"),
    (["(()", ")("], "No"),
    (["(()())", "()"], "Yes"),
    (["((()))", "()"], "Yes"),
    (["(())", "((()))"], "Yes")
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
    try:
        match_parens(["(", ")", "("])
    except (IndexError, ValueError):
        pass
    else:
        pytest.fail("Expected IndexError or ValueError")

def test_match_parens_invalid_input():
    with pytest.raises(TypeError):
        match_parens(None)

def test_match_parens_invalid_characters():
    assert match_parens(["a", "b"]) == "No"
    assert match_parens(["(a)", "b"]) == "No"
    assert match_parens(["[", "]"]) == "No"