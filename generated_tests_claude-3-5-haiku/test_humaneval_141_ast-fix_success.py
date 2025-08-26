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

def test_file_name_check_valid_txt_file():
    assert file_name_check('document.txt') == 'Yes'

def test_file_name_check_valid_exe_file():
    assert file_name_check('program.exe') == 'Yes'

def test_file_name_check_valid_dll_file():
    assert file_name_check('library.dll') == 'Yes'

def test_file_name_check_valid_file_with_numbers():
    assert file_name_check('doc123.txt') == 'Yes'

def test_file_name_check_invalid_file_too_many_numbers():
    assert file_name_check('doc1234.txt') == 'No'

def test_file_name_check_invalid_extension():
    assert file_name_check('file.pdf') == 'No'

def test_file_name_check_no_extension():
    assert file_name_check('filename') == 'No'

def test_file_name_check_multiple_extensions():
    assert file_name_check('file.name.txt') == 'No'

def test_file_name_check_empty_filename():
    assert file_name_check('.txt') == 'No'

def test_file_name_check_non_alpha_start():
    assert file_name_check('1document.txt') == 'No'

@pytest.mark.parametrize("filename,expected", [
    ('valid.txt', 'Yes'),
    ('program.exe', 'Yes'),
    ('lib123.dll', 'Yes'),
    ('file.pdf', 'No'),
    ('1invalid.txt', 'No'),
    ('doc1234.txt', 'No'),
    ('file.name.txt', 'No'),
    ('.txt', 'No')
])
def test_file_name_check_parametrized(filename, expected):
    assert file_name_check(filename) == expected
