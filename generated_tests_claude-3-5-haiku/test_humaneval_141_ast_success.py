# Test cases for HumanEval/141
# Generated using Claude API


def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """

    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst) != 2:
        return 'No'
    if not lst[1] in suf:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    return 'Yes'


# Generated test cases:
import pytest

def test_file_name_check_valid_cases():
    assert file_name_check('document.txt') == 'Yes'
    assert file_name_check('program.exe') == 'Yes'
    assert file_name_check('library.dll') == 'Yes'
    assert file_name_check('a123.txt') == 'Yes'

def test_file_name_check_invalid_cases():
    assert file_name_check('document.pdf') == 'No'
    assert file_name_check('document') == 'No'
    assert file_name_check('.txt') == 'No'
    assert file_name_check('1document.txt') == 'No'

def test_file_name_check_digit_limit():
    assert file_name_check('a1234.txt') == 'No'
    assert file_name_check('a123.txt') == 'Yes'

@pytest.mark.parametrize("filename,expected", [
    ('test.txt', 'Yes'),
    ('program.exe', 'Yes'),
    ('lib.dll', 'Yes'),
    ('a1b2c3.txt', 'Yes'),
    ('invalid.pdf', 'No'),
    ('123.txt', 'No'),
    ('.txt', 'No'),
    ('document', 'No'),
    ('a1234.txt', 'No')
])
def test_file_name_check_parametrized(filename, expected):
    assert file_name_check(filename) == expected
