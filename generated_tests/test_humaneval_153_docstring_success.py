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
    ("my_class", ["AA", "Be", "CC"], "my_class.AA"),
    ("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"], "Slices.SErviNGSliCes"),
    ("", ["A", "B", "C"], ".A"),
    ("Class", ["UPPER", "lower", "MiXeD"], "Class.UPPER"),
    ("Test", ["AAA", "aaa", "BBB"], "Test.AAA"),
    ("Sample", ["A1B2", "a1b2", "123"], "Sample.A1B2"),
    ("Module", ["TEST", "test", "Test"], "Module.TEST"),
    ("Class", ["Ab", "aB", "ab"], "Class.Ab"),
    ("System", ["SYStem", "system", "SYSTEM"], "System.SYSTEM"),
    ("Base", ["", "A", "a"], "Base.A")
])
def test_multiple_cases(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

def test_single_extension():
    assert Strongest_Extension("Class", ["Extension"]) == "Class.Extension"

def test_same_strength_first_wins():
    assert Strongest_Extension("Test", ["AA", "BB", "CC"]) == "Test.AA"

def test_special_characters():
    assert Strongest_Extension("Class", ["A_B", "a-b", "A@B"]) == "Class.A_B"

def test_numeric_extensions():
    assert Strongest_Extension("Numbers", ["123", "456", "789"]) == "Numbers.123"

def test_empty_class_name():
    assert Strongest_Extension("", ["Extension"]) == ".Extension"

def test_mixed_case_extensions():
    assert Strongest_Extension("Mix", ["aBcDeF", "AbCdEf", "ABCDEF"]) == "Mix.ABCDEF"

def test_single_character_extensions():
    assert Strongest_Extension("Char", ["A", "b", "C"]) == "Char.A"
