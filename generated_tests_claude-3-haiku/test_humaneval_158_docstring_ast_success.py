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

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """

    if not words:
        return ""
    return sorted(words, key=lambda x: (-len(set(x)), x))[0]

def test_find_max_empty_list():
    assert find_max([]) == ""

@pytest.mark.parametrize("words,expected", [
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    (["abc", "def", "ghi"], "abc"),
    (["hello", "world", "python"], "python"),
    (["aaa", "bb", "c"], "aaa"),
])
def test_find_max_valid_inputs(words, expected):
    assert find_max(words) == expected

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_all_unique_characters():
    assert find_max(["a", "b", "c", "d"]) == "a"

def test_find_max_all_same_characters():
    assert find_max(["aaa", "aaa", "aaa"]) == "aaa"

def test_find_max_case_sensitivity():
    assert find_max(["Abc", "aBc", "abC"]) == "Abc"