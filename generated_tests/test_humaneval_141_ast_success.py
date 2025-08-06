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

@pytest.mark.parametrize("file_name,expected", [
    ("file.txt", "Yes"),
    ("document.exe", "Yes"),
    ("program.dll", "Yes"),
    ("abc123.txt", "Yes"),
    ("test12.exe", "Yes"),
    ("a.txt", "Yes"),
    ("file.doc", "No"),
    ("file.pdf", "No"),
    (".txt", "No"),
    ("file.", "No"),
    ("file", "No"),
    ("123file.txt", "No"),
    ("file..txt", "No"),
    ("file.txt.exe", "No"),
    ("file1234.txt", "No"),
    ("@file.txt", "No"),
    ("file@.txt", "Yes"),
    ("a123.txt", "Yes"),
    ("abc1234.exe", "No"),
    ("", "No"),
    ("..", "No"),
    ("file.TXT", "No"),
    ("file.EXE", "No"),
    ("file.DLL", "No"),
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected

def test_file_name_check_empty_string():
    assert file_name_check("") == "No"

def test_file_name_check_single_dot():
    assert file_name_check(".") == "No"

def test_file_name_check_multiple_dots():
    assert file_name_check("file...txt") == "No"

def test_file_name_check_special_chars():
    assert file_name_check("file#.txt") == "Yes"
    assert file_name_check("file$.txt") == "Yes"
    assert file_name_check("file%.txt") == "Yes"

def test_file_name_check_max_digits():
    assert file_name_check("file123.txt") == "Yes"
    assert file_name_check("file1234.txt") == "No"

def test_file_name_check_spaces():
    assert file_name_check("file name.txt") == "Yes"
    assert file_name_check(" file.txt") == "No"
