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

@pytest.mark.parametrize("words,expected", [
    (["hello", "world", "python"], "python"),
    (["cat", "dog", "rat"], "cat"),
    (["aaa", "bbb", "ccc"], "aaa"),
    (["abcde", "abc", "abcd"], "abcde"),
    (["aaaa", "bbbb", "cccc", "dddd"], "aaaa"),
    (["test", "tester", "testing"], "testing"),
    (["aabbcc", "abc", "aabb"], "aabbcc"),
    (["python", "pythons", "pythonic"], "pythonic"),
    (["a", "aa", "aaa"], "aaa"),
    (["abcdef", "fedcba", "abcdef"], "abcdef"),
])
def test_find_max_normal_cases(words, expected):
    assert find_max(words) == expected

@pytest.mark.parametrize("words,expected", [
    (["a"], "a"),
    (["hello"], "hello"),
    (["x"], "x"),
])
def test_find_max_single_word(words, expected):
    assert find_max(words) == expected

@pytest.mark.parametrize("words,expected", [
    (["", "a", "b"], "a"),
    (["", "", "c"], "c"),
    (["a", "", ""], "a"),
])
def test_find_max_empty_strings(words, expected):
    assert find_max(words) == expected

def test_find_max_empty_list():
    with pytest.raises(IndexError):
        find_max([])

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    42.0,
    (1, 2, 3),
])
def test_find_max_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        find_max(invalid_input)

@pytest.mark.parametrize("words,expected", [
    (["AAA", "aaa", "AaA"], "AaA"),
    (["Python", "PYTHON", "python"], "PYTHON"),
])
def test_find_max_case_sensitivity(words, expected):
    assert find_max(words) == expected

@pytest.mark.parametrize("words,expected", [
    (["12345", "123", "1234"], "12345"),
    (["!@#", "$%^", "&*("], "!@#"),
])
def test_find_max_special_characters(words, expected):
    assert find_max(words) == expected