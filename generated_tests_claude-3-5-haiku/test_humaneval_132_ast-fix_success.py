# Test cases for HumanEval/132
# Generated using Claude API


def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''

    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        if string[i] == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2

    


# Generated test cases:
import pytest

def is_nested(string):
    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        if string[i] == '[':
            opening_bracket_index.append(i)
        elif string[i] == ']':
            closing_bracket_index.append(i)
    
    if len(opening_bracket_index) <= 1 or len(closing_bracket_index) <= 1:
        return False
    
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    
    for idx in opening_bracket_index:
        while i < l and idx > closing_bracket_index[i]:
            i += 1
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    
    return cnt >= 2

def test_is_nested_multiple_nested_brackets():
    assert is_nested("[[]]") == True
    assert is_nested("[[][]]") == True
    assert is_nested("[[[]]]") == True

def test_is_nested_single_brackets():
    assert is_nested("[]") == False
    assert is_nested("[a]") == False

def test_is_nested_no_brackets():
    assert is_nested("abc") == False
    assert is_nested("") == False

def test_is_nested_complex_cases():
    assert is_nested("[a[b]c]") == True
    assert is_nested("a[b[c]]d") == True
    assert is_nested("[a]b[c]") == False

@pytest.mark.parametrize("input_string,expected", [
    ("[[]]", True),
    ("[[][]]", True),
    ("[[[]]]", True),
    ("[]", False),
    ("[a]", False),
    ("abc", False),
    ("", False),
    ("[a[b]c]", True),
    ("a[b[c]]d", True),
    ("[a]b[c]", False)
])
def test_is_nested_parametrized(input_string, expected):
    assert is_nested(input_string) == expected