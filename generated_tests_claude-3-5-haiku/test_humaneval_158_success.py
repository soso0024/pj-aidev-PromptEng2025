# Test cases for HumanEval/158
# Generated using Claude API


def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    return sorted(words, key = lambda x: (-len(set(x)), x))[0]


# Generated test cases:
import pytest

def test_find_max_basic_case():
    words = ['hello', 'world', 'python']
    assert find_max(words) == 'python'

def test_find_max_unique_chars():
    words = ['abc', 'def', 'abcdef']
    assert find_max(words) == 'abcdef'

def test_find_max_same_unique_chars_length():
    words = ['abc', 'cab', 'bca']
    assert find_max(words) == 'abc'

def test_find_max_single_word():
    words = ['hello']
    assert find_max(words) == 'hello'

def test_find_max_empty_list():
    with pytest.raises(IndexError):
        find_max([])

@pytest.mark.parametrize("words,expected", [
    (['apple', 'banana', 'cherry'], 'cherry'),
    (['short', 'longer', 'longest'], 'longest'),
    (['aaa', 'bbb', 'ccc'], 'aaa')
])
def test_find_max_parametrized(words, expected):
    assert find_max(words) == expected

def test_find_max_case_sensitive():
    words = ['Apple', 'apple', 'APPLE']
    assert find_max(words) == 'APPLE'

def test_find_max_with_numbers_and_symbols():
    words = ['hello123', 'world!', 'python@']
    assert find_max(words) == 'hello123'