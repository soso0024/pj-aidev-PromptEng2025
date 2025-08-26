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
    assert find_max([]) is None

def test_find_max_single_word():
    assert find_max(['apple']) == 'apple'

def test_find_max_multiple_words():
    assert find_max(['apple', 'banana', 'cherry']) == 'apple'

@pytest.mark.parametrize("words,expected", [
    (['apple', 'banana', 'cherry', 'date'], 'date'),
    (['hello', 'world', 'python', 'java'], 'world'),
    (['aaa', 'bb', 'c', 'dddd'], 'dddd'),
    (['abcd', 'abc', 'ab', 'a'], 'abcd')
])
def test_find_max_with_different_inputs(words, expected):
    assert find_max(words) == expected

def test_find_max_with_duplicate_words():
    assert find_max(['apple', 'banana', 'apple', 'cherry']) == 'cherry'

def test_find_max_with_all_unique_lengths():
    assert find_max(['a', 'bb', 'ccc', 'dddd']) == 'dddd'

def find_max(words):
    if not words:
        return None
    return sorted(words, key=lambda x: (-len(set(x)), x))[0]