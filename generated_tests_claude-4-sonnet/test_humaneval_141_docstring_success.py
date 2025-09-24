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
    ("example.txt", "Yes"),
    ("test.exe", "Yes"),
    ("program.dll", "Yes"),
    ("a.txt", "Yes"),
    ("file123.txt", "Yes"),
    ("test12.exe", "Yes"),
    ("prog3.dll", "Yes"),
    ("1example.dll", "No"),
    ("example.doc", "No"),
    ("example", "No"),
    (".txt", "No"),
    ("example.", "No"),
    ("example.txt.exe", "No"),
    ("ex.am.ple.txt", "No"),
    ("", "No"),
    ("example.TXT", "No"),
    ("example.EXE", "No"),
    ("example.DLL", "No"),
    ("EXAMPLE.txt", "Yes"),
    ("Example.exe", "Yes"),
    ("file1234.txt", "No"),
    ("file12345.dll", "No"),
    ("test0000.exe", "No"),
    ("_test.txt", "No"),
    ("9test.txt", "No"),
    ("-file.exe", "No"),
    ("file@.dll", "Yes"),
    ("file#.txt", "Yes"),
    ("file$.exe", "Yes"),
    ("file%.dll", "Yes"),
    ("file&.txt", "Yes"),
    ("file*.exe", "Yes"),
    ("file(.dll", "Yes"),
    ("file).txt", "Yes"),
    ("file+.exe", "Yes"),
    ("file=.dll", "Yes"),
    ("file[.txt", "Yes"),
    ("file].exe", "Yes"),
    ("file{.dll", "Yes"),
    ("file}.txt", "Yes"),
    ("file|.exe", "Yes"),
    ("file;.dll", "Yes"),
    ("file:.txt", "Yes"),
    ("file'.exe", "Yes"),
    ('file".dll', "Yes"),
    ("file,.txt", "Yes"),
    ("file<.exe", "Yes"),
    ("file>.dll", "Yes"),
    ("file?.txt", "Yes"),
    ("file/.exe", "Yes"),
    ("file\\.dll", "Yes"),
    ("file~.txt", "Yes"),
    ("file`.exe", "Yes"),
    ("file!.dll", "Yes"),
    ("a1b2c3.txt", "Yes"),
    ("a1b2c3d4.txt", "No"),
    ("abc.xyz", "No"),
    ("test..txt", "No"),
    ("..txt", "No"),
    ("test..", "No"),
    ("..", "No"),
    (".", "No"),
    ("test.txt.backup", "No"),
    ("backup.test.txt", "No")
])
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected

def test_empty_string():
    assert file_name_check("") == "No"

def test_only_dot():
    assert file_name_check(".") == "No"

def test_multiple_dots():
    assert file_name_check("a.b.c") == "No"
    assert file_name_check("test.txt.exe") == "No"
    assert file_name_check("file.name.txt") == "No"

def test_no_dot():
    assert file_name_check("filename") == "No"
    assert file_name_check("test") == "No"

def test_empty_name_part():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"
    assert file_name_check(".dll") == "No"

def test_empty_extension():
    assert file_name_check("test.") == "No"
    assert file_name_check("file.") == "No"

def test_invalid_extension():
    assert file_name_check("test.pdf") == "No"
    assert file_name_check("file.doc") == "No"
    assert file_name_check("program.py") == "No"

def test_case_sensitive_extension():
    assert file_name_check("test.TXT") == "No"
    assert file_name_check("file.EXE") == "No"
    assert file_name_check("program.DLL") == "No"

def test_starts_with_digit():
    assert file_name_check("1test.txt") == "No"
    assert file_name_check("9file.exe") == "No"
    assert file_name_check("0program.dll") == "No"

def test_starts_with_special_char():
    assert file_name_check("_test.txt") == "No"
    assert file_name_check("-file.exe") == "No"
    assert file_name_check("@program.dll") == "No"

def test_too_many_digits():
    assert file_name_check("test1234.txt") == "No"
    assert file_name_check("file12345.exe") == "No"
    assert file_name_check("a1b2c3d4.dll") == "No"

def test_exactly_three_digits():
    assert file_name_check("test123.txt") == "Yes"
    assert file_name_check("file321.exe") == "Yes"
    assert file_name_check("a1b2c3.dll") == "Yes"

def test_valid_cases():
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("Z.exe") == "Yes"
    assert file_name_check("test.dll") == "Yes"
    assert file_name_check("MyFile123.txt") == "Yes"
