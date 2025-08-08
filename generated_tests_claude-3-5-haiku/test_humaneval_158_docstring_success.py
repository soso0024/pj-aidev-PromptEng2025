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
    if not words:
        return ""
    return sorted(words, key = lambda x: (-len(set(x)), x))[0]

def test_find_max_normal_cases():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_lexicographic_order():
    assert find_max(["abc", "cab", "bca"]) == "abc"
    assert find_max(["hello", "world", "python"]) == "python"

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["test"]) == "test"

def test_find_max_duplicate_unique_chars():
    assert find_max(["abcd", "dcba", "efgh"]) == "abcd"

@pytest.mark.parametrize("words,expected", [
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    (["abc", "cab", "bca"], "abc"),
    ([], ""),
    (["test"], "test")
])
def test_find_max_parametrized(words, expected):
    assert find_max(words) == expected