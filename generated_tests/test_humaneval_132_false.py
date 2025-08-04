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

@pytest.mark.parametrize("input_str,expected", [
    ("[[]]", True),
    ("[[][]]", True),
    ("[][]", False),
    ("[[[]]]", True),
    ("[[[", False),
    ("]]]", False),
    ("", False),
    ("[]", False),
    ("[[][[]]]", True),
    ("[[]][]", False),
    ("[[]][][]", False),
    ("[", False),
    ("]", False),
    ("[[[][]]]", True),
    ("[[][][]]", True),
    ("[[[]]][]", False),
    ("[[][[][]]]", True),
    ("[[[[]]]]", True),
    ("[[]][[]]", False),
    ("[][][]", False)
])
def test_is_nested(input_str, expected):
    result = is_nested(input_str)
    if not is_valid_brackets(input_str):
        assert not result
    else:
        assert result == expected

def is_valid_brackets(s):
    stack = []
    for char in s:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def test_is_nested_empty_string():
    assert not is_nested("")

def test_is_nested_single_bracket():
    assert not is_nested("[")
    assert not is_nested("]")

def test_is_nested_single_pair():
    assert not is_nested("[]")

def test_is_nested_multiple_single_pairs():
    assert not is_nested("[][]")
    assert not is_nested("[][][]")

def test_is_nested_complex_valid():
    assert is_nested("[[[][]]]")
    assert is_nested("[[][[]]]")
    assert is_nested("[[[][]][]]")

def test_is_nested_unbalanced():
    assert not is_nested("[[[")
    assert not is_nested("]]]")
    assert not is_nested("[[]")
    assert not is_nested("[]]")