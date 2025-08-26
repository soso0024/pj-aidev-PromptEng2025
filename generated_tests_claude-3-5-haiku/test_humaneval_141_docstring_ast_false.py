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
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("test123.dll") == 'Yes'
    assert file_name_check("code12.exe") == 'Yes'
    assert file_name_check("UPPERCASE.DLL") == 'Yes'

def test_file_name_check_invalid_suffix():
    assert file_name_check("file.pdf") == 'No'
    assert file_name_check("document.docx") == 'No'

def test_file_name_check_multiple_dots():
    assert file_name_check("file.name.txt") == 'No'
    assert file_name_check("file.with.multiple.dots.txt") == 'No'

def test_file_name_check_empty_name():
    assert file_name_check(".txt") == 'No'

def test_file_name_check_non_alpha_start():
    assert file_name_check("1example.txt") == 'No'
    assert file_name_check("_test.dll") == 'No'

def test_file_name_check_too_many_digits():
    assert file_name_check("file1234.txt") == 'No'
    assert file_name_check("code5678.exe") == 'No'

@pytest.mark.parametrize("filename,expected", [
    ("valid.txt", 'Yes'),
    ("test123.dll", 'Yes'),
    ("code12.exe", 'Yes'),
    ("1invalid.txt", 'No'),
    ("file.with.dots.txt", 'No'),
    ("toolongdigits1234.exe", 'No'),
    (".missingname.txt", 'No'),
    ("valid_name.txt", 'Yes'),
    ("UPPERCASE.DLL", 'Yes')
])
def test_file_name_check_parametrized(filename, expected):
    assert file_name_check(filename) == expected