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

def file_name_check(file_name):
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

@pytest.mark.parametrize("file_name,expected", [
    ("test.txt", "Yes"),
    ("example.exe", "Yes"),
    ("program.dll", "Yes"),
    ("a.txt", "Yes"),
    ("file123.exe", "Yes"),
    ("test1.dll", "Yes"),
    ("abc123.txt", "Yes"),
    ("file12.exe", "Yes"),
    ("test.pdf", "No"),
    ("file.doc", "No"),
    ("test.xyz", "No"),
    ("", "No"),
    ("test", "No"),
    ("test.txt.backup", "No"),
    ("file..txt", "No"),
    ("test.txt.exe", "No"),
    (".txt", "No"),
    (".exe", "No"),
    (".dll", "No"),
    ("1test.txt", "No"),
    ("2file.exe", "No"),
    ("9program.dll", "No"),
    ("_test.txt", "No"),
    ("-file.exe", "No"),
    ("@program.dll", "No"),
    ("test1234.txt", "No"),
    ("file12345.exe", "No"),
    ("program9876.dll", "No"),
    ("a1b2c3d4.txt", "No"),
    ("test123456.exe", "No"),
    ("file0000.dll", "No"),
    ("a1b2c3.txt", "Yes"),
    ("test000.exe", "Yes"),
    ("file999.dll", "Yes"),
    ("A.txt", "Yes"),
    ("Z.exe", "Yes"),
    ("MyFile.dll", "Yes"),
    ("Test123.txt", "Yes"),
    ("FILE.exe", "Yes"),
    ("Program1.dll", "Yes"),
    ("a0b1c2.txt", "Yes"),
    ("x9y8z7.exe", "Yes"),
    ("File1a2b.dll", "Yes"),
    ("test.", "No"),
    (".test", "No"),
    (".", "No"),
    ("..", "No"),
    ("test.TXT", "No"),
    ("test.EXE", "No"),
    ("test.DLL", "No"),
    ("test.Txt", "No"),
    ("test.Exe", "No"),
    ("test.Dll", "No")
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected

def test_empty_string():
    assert file_name_check("") == "No"

def test_single_character_valid():
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("z.exe") == "Yes"
    assert file_name_check("A.dll") == "Yes"

def test_single_character_invalid():
    assert file_name_check("1.txt") == "No"
    assert file_name_check("_.exe") == "No"
    assert file_name_check("-.dll") == "No"

def test_exactly_three_digits():
    assert file_name_check("a123.txt") == "Yes"
    assert file_name_check("test000.exe") == "Yes"
    assert file_name_check("file999.dll") == "Yes"

def test_more_than_three_digits():
    assert file_name_check("a1234.txt") == "No"
    assert file_name_check("test0000.exe") == "No"
    assert file_name_check("file99999.dll") == "No"

def test_no_extension():
    assert file_name_check("test") == "No"
    assert file_name_check("file123") == "No"
    assert file_name_check("a") == "No"

def test_multiple_dots():
    assert file_name_check("test.backup.txt") == "No"
    assert file_name_check("file.old.exe") == "No"
    assert file_name_check("a.b.c.dll") == "No"

def test_consecutive_dots():
    assert file_name_check("test..txt") == "No"
    assert file_name_check("file...exe") == "No"
    assert file_name_check("a..dll") == "No"
