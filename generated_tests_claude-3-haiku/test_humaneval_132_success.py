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

def test_is_nested():
    assert is_nested('a[b]c[d]e') == True
    assert is_nested('a[b[c]]d') == True
    assert is_nested('a[b]c[d]e[f]') == True
    assert is_nested('a[b]c[d') == False
    assert is_nested('a[b]c]d') == False
    assert is_nested('a[b]c[d]') == True
    assert is_nested('a[b]c') == False
    assert is_nested('a[b]') == False
    assert is_nested('a') == False
    assert is_nested('') == False

@pytest.mark.parametrize("input,expected", [
    ('a[b]c[d]e', True),
    ('a[b[c]]d', True),
    ('a[b]c[d]e[f]', True),
    ('a[b]c[d', False),
    ('a[b]c]d', False),
    ('a[b]c[d]', True),
    ('a[b]c', False),
    ('a[b]', False),
    ('a', False),
    ('', False)
])
def test_is_nested_parametrized(input, expected):
    assert is_nested(input) == expected