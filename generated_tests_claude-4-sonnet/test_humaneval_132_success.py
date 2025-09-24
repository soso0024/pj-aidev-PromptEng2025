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

@pytest.mark.parametrize("input_string,expected", [
    ("", False),
    ("[", False),
    ("]", False),
    ("[]", False),
    ("[[", False),
    ("]]", False),
    ("[[]", False),
    ("[][", False),
    ("[[]]", True),
    ("[[][]]", True),
    ("[[[]]]", True),
    ("[][][]", True),
    ("[[][][]]", True),
    ("[[[", False),
    ("]]]", False),
    ("[[[]", False),
    ("[]]", False),
    ("][][", False),
    ("[[[]]", True),
    ("[[]]]]", True),
    ("[[[[]]]]", True),
    ("[[][][][[]]", True),
    ("[[][][[]]", True),
    ("[[]][[]]", True),
    ("[[][[]]]", True),
    ("[[[[[[]]]]]]", True),
    ("][", False),
    ("][][][][", True),
    ("[[[[[", False),
    ("]]]]]", False),
    ("[[[[[]", False),
    ("[]]]]", False)
])
def test_is_nested_parametrized(input_string, expected):
    assert is_nested(input_string) == expected

def test_empty_string():
    assert is_nested("") == False

def test_single_opening_bracket():
    assert is_nested("[") == False

def test_single_closing_bracket():
    assert is_nested("]") == False

def test_simple_pair():
    assert is_nested("[]") == False

def test_nested_pair():
    assert is_nested("[[]]") == True

def test_multiple_nested():
    assert is_nested("[[[]]]]") == True

def test_no_nesting_multiple_pairs():
    assert is_nested("][][") == False

def test_mixed_valid_nesting():
    assert is_nested("[[]][[]]") == True

def test_unbalanced_more_opening():
    assert is_nested("[[[") == False

def test_unbalanced_more_closing():
    assert is_nested("]]]") == False

def test_complex_nested():
    assert is_nested("[[[[[[]]]]]]") == True

def test_invalid_order():
    assert is_nested("][") == False