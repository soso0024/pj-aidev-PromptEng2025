# Test cases for HumanEval/86
# Generated using Claude API


def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """

    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])


# Generated test cases:
from functools import reduce

def test_anti_shuffle(input, expected):
    assert ''.join(sorted(list(i)) for i in input.split(' ')) == expected

def test_anti_shuffle_edge_cases():
    assert anti_shuffle('') == ''
    assert anti_shuffle('   ') == '   '

def test_anti_shuffle_error_handling():
    with pytest.raises(TypeError):
        anti_shuffle(123)
    with pytest.raises(TypeError):
        anti_shuffle(None)

def anti_shuffle(s):
    return ' '.join(''.join(sorted(list(i))) for i in s.split(' '))