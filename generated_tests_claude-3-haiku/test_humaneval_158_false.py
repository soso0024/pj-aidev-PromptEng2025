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

def test_find_max_empty_list():
    assert find_max([]) == ''

@pytest.mark.parametrize("words,expected", [
    (['apple', 'banana', 'cherry'], 'cherry'),
    (['hello', 'world', 'python'], 'python'),
    (['aaa', 'bb', 'c'], 'aaa'),
    (['abcd', 'abc', 'ab'], 'abcd'),
])
def test_find_max_normal_cases(words, expected):
    assert find_max(words) == expected

def test_find_max_single_element():
    assert find_max(['test']) == 'test'

def test_find_max_all_equal_length():
    assert find_max(['abc', 'def', 'ghi']) == 'abc'

def test_find_max_all_unique_chars():
    assert find_max(['a', 'b', 'c']) == 'a'

def test_find_max_all_same_chars():
    assert find_max(['aaa', 'aaa', 'aaa']) == 'aaa'

def test_find_max_mixed_case():
    assert find_max(['Apple', 'BANANA', 'cherry']) == 'Apple'

def test_find_max_non_string_element():
    with pytest.raises(TypeError):
        find_max([1, 'hello', 'world'])

def find_max(words):
    if not words:
        return ''
    return sorted(words, key=lambda x: (-len(set(x)), x))[0]