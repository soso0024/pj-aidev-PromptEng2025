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

def Strongest_Extension(class_name, extensions):
    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans

def test_example_from_docstring():
    assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"

def test_example_from_docstring_2():
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

def test_single_extension():
    assert Strongest_Extension("TestClass", ["Extension"]) == "TestClass.Extension"

def test_all_uppercase():
    assert Strongest_Extension("Class", ["ABC", "DEF", "GHI"]) == "Class.ABC"

def test_all_lowercase():
    assert Strongest_Extension("Class", ["abc", "def", "ghi"]) == "Class.abc"

def test_mixed_case_extensions():
    assert Strongest_Extension("MyClass", ["AbC", "dEf", "GhI"]) == "MyClass.AbC"

def test_extensions_with_numbers():
    assert Strongest_Extension("Class", ["Abc123", "DEF456", "ghi789"]) == "Class.DEF456"

def test_extensions_with_special_characters():
    assert Strongest_Extension("Class", ["Ab@c", "DE#F", "gh$i"]) == "Class.DE#F"

def test_tie_first_wins():
    assert Strongest_Extension("Class", ["AB", "CD", "EF"]) == "Class.AB"

def test_negative_strengths():
    assert Strongest_Extension("Class", ["abc", "def", "Ghi"]) == "Class.Ghi"

def test_zero_strength():
    assert Strongest_Extension("Class", ["Aa", "Bb", "Cc"]) == "Class.Aa"

def test_empty_strings():
    assert Strongest_Extension("Class", ["", "A", "a"]) == "Class.A"

def test_only_special_characters():
    assert Strongest_Extension("Class", ["@#$", "123", "!!!"]) == "Class.@#$"

def test_long_extensions():
    assert Strongest_Extension("Class", ["ABCDEFGHIJKLMNOP", "abcdefghijklmnop", "AaBbCcDdEeFf"]) == "Class.ABCDEFGHIJKLMNOP"

@pytest.mark.parametrize("class_name,extensions,expected", [
    ("Test", ["A"], "Test.A"),
    ("MyClass", ["aB", "Ab"], "MyClass.aB"),
    ("Class", ["ABC", "abc", "AbC"], "Class.ABC"),
    ("Name", ["123ABC", "456def", "789GHI"], "Name.123ABC"),
])
def test_parametrized_cases(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

def test_complex_mixed_case():
    assert Strongest_Extension("ComplexClass", ["AbCdEfGhIjKlMnOp", "ABCDEFGH", "abcdefgh"]) == "ComplexClass.ABCDEFGH"

def test_strength_calculation():
    assert Strongest_Extension("Test", ["abc", "AaBbCc", "ABC"]) == "Test.ABC"

def test_identical_extensions():
    assert Strongest_Extension("Class", ["Same", "Same", "Same"]) == "Class.Same"