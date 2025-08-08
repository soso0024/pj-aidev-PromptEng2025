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

def test_find_max_single_word():
    assert find_max(['apple']) == 'apple'

def test_find_max_multiple_words():
    assert find_max(['apple', 'banana', 'cherry']) == 'cherry'

def test_find_max_words_with_same_length():
    assert find_max(['abc', 'def', 'ghi']) == 'abc'

def test_find_max_words_with_same_unique_chars():
    assert find_max(['aaa', 'bbb', 'ccc']) == 'aaa'

@pytest.mark.parametrize("words,expected", [
    (['apple', 'banana', 'cherry', 'date'], 'date'),
    (['hello', 'world', 'python', 'java'], 'world'),
    (['aaa', 'bbb', 'ccc', 'ddd'], 'aaa'),
    (['xyz', 'abc', 'def', 'ghi'], 'xyz'),
    (['a', 'bb', 'ccc', 'dddd'], 'dddd')
])
def test_find_max_with_parametrize(words, expected):
    assert find_max(words) == expected

def test_find_max_with_non_string_elements():
    with pytest.raises(TypeError):
        find_max([1, 2, 3, 4])

def test_find_max_with_mixed_types():
    with pytest.raises(TypeError):
        find_max(['apple', 'banana', 123, 'cherry'])

def find_max(words):
    if not words:
        return ''
    return sorted(words, key=lambda x: (-len(set(x)), x))[0]