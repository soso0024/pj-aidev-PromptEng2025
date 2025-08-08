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
    ("example.txt", "Yes"),
    ("test.exe", "Yes"),
    ("program.dll", "Yes"),
    ("abc123.txt", "Yes"),
    ("test1.exe", "Yes"),
    ("a.txt", "Yes"),
    (".txt", "No"),
    ("test.", "No"),
    ("test", "No"),
    ("test.doc", "No"),
    ("1test.txt", "No"),
    ("test.txt.exe", "No"),
    ("test1234.txt", "No"),
    ("@test.txt", "No"),
    ("test@123.exe", "Yes"),
    ("", "No"),
    ("test..txt", "No"),
    ("a1b2c3.dll", "Yes"),
    ("a1b2c3d4.dll", "No"),
    ("test space.txt", "Yes"),
    ("test_file.exe", "Yes"),
    ("test-file.dll", "Yes")
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected

def test_file_name_check_empty_string():
    assert file_name_check("") == "No"

def test_file_name_check_single_dot():
    assert file_name_check(".") == "No"

def test_file_name_check_multiple_dots():
    assert file_name_check("test.txt.exe") == "No"

def test_file_name_check_special_chars():
    assert file_name_check("test#.txt") == "Yes"
    assert file_name_check("test$.exe") == "Yes"
    assert file_name_check("test%.dll") == "Yes"

def test_file_name_check_max_digits():
    assert file_name_check("test123.txt") == "Yes"
    assert file_name_check("test1234.txt") == "No"

def test_file_name_check_invalid_extension():
    assert file_name_check("test.pdf") == "No"
    assert file_name_check("test.docx") == "No"
    assert file_name_check("test.jpg") == "No"
