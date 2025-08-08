# Test cases for HumanEval/153
# Generated using Claude API


def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """

    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans



# Generated test cases:
import pytest

def test_basic_case():
    assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"

def test_all_uppercase():
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

@pytest.mark.parametrize("class_name,extensions,expected", [
    ("class", ["AAA", "bbb", "CCC"], "class.AAA"),
    ("my_class", ["lower", "UPPER", "MiXeD"], "my_class.UPPER"),
    ("Test", ["abc", "ABC", "123"], "Test.ABC"),
    ("Class", ["a", "B", "C"], "Class.B"),
    ("Module", ["", "A", "b"], "Module.A"),
    ("System", ["aA", "Aa", "aa"], "System.aA"),
    ("Base", ["Extension1", "EXTENSION2", "eXtEnSiOn3"], "Base.EXTENSION2"),
    ("Main", ["Test123", "TEST456", "test789"], "Main.TEST456"),
    ("App", ["A1b2C3", "a1B2c3", "A1B2C3"], "App.A1B2C3"),
    ("Program", ["!!!ABC!!!", "...abc...", "___ABC___"], "Program.!!!ABC!!!")
])
def test_multiple_cases(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

def test_single_extension():
    assert Strongest_Extension("Class", ["Extension"]) == "Class.Extension"

def test_same_strength_first_wins():
    assert Strongest_Extension("Test", ["AA", "BB", "CC"]) == "Test.AA"

def test_special_characters():
    assert Strongest_Extension("Class", ["A@B#C", "a$b%c", "123"]) == "Class.A@B#C"

def test_empty_class_name():
    assert Strongest_Extension("", ["ABC", "def"]) == ".ABC"

def test_numbers_only():
    assert Strongest_Extension("Math", ["123", "456", "789"]) == "Math.123"

def test_mixed_case_with_numbers():
    assert Strongest_Extension("Code", ["Test123ABC", "test123abc", "TEST123ABC"]) == "Code.TEST123ABC"

def test_whitespace():
    assert Strongest_Extension("Space", ["A B C", "a b c", "A B c"]) == "Space.A B C"
