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
    ("file.exe", "Yes"),
    ("program.dll", "Yes"),
    ("test123.txt", "Yes"),
    ("A.txt", "Yes"),
    ("abc123.exe", "Yes"),
    ("1example.dll", "No"),
    ("123.txt", "No"),
    (".txt", "No"),
    ("file.", "No"),
    ("file.doc", "No"),
    ("file.txt.exe", "No"),
    ("file", "No"),
    ("1234.txt", "No"),
    ("test1234.exe", "No"),
    ("test.1234", "No"),
    ("test..txt", "No"),
    ("@test.txt", "No"),
    ("test@123.txt", "Yes"),
    ("a.txt", "Yes"),
    ("Z.dll", "Yes"),
    ("file.PDF", "No"),
    ("file.TXT", "No"),
    ("", "No"),
    ("file.txt ", "No"),
    (" file.txt", "No"),
    ("file space.txt", "Yes"),
    ("file_123.exe", "Yes"),
    ("file-name.dll", "Yes"),
    ("file!.txt", "Yes")
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected

def test_file_name_check_none():
    with pytest.raises(AttributeError):
        file_name_check(None)

def test_file_name_check_non_string():
    with pytest.raises(AttributeError):
        file_name_check(123)
