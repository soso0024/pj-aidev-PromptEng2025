# Test cases for HumanEval/101
# Generated using Claude API


def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    if not s:
        return []

    s_list = []

    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()


# Generated test cases:
def words_string(s):
    if not s:
        return []

    s_list = []
    for char in s:
        if char == ',':
            s_list.append(' ')
        else:
            s_list.append(char)

    return ''.join(s_list).split()

def test_words_string_empty_string():
    assert words_string("") == []

def test_words_string_single_word():
    assert words_string("hello") == ["hello"]

def test_words_string_multiple_words_comma_separated():
    assert words_string("one, two, three") == ["one", "two", "three"]

def test_words_string_multiple_words_space_separated():
    assert words_string("apple banana cherry") == ["apple", "banana", "cherry"]

def test_words_string_mixed_comma_and_space_separated():
    assert words_string("red, green blue, yellow") == ["red", "green", "blue", "yellow"]

def test_words_string_leading_and_trailing_spaces():
    assert words_string("  hello, world  ") == ["hello", "world"]

def test_words_string_consecutive_commas():
    assert words_string("one,,two,three") == ["one", "two", "three"]

def test_words_string_consecutive_spaces():
    assert words_string("apple   banana   cherry") == ["apple", "banana", "cherry"]

def test_words_string_all_commas():
    assert words_string(",,,,,") == []

def test_words_string_all_spaces():
    assert words_string("   ") == []