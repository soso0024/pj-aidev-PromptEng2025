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

def test_strongest_extension_basic():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_mixed_case():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_equal_strength():
    assert Strongest_Extension('Test', ['AB', 'AB']) == 'Test.AB'

def test_strongest_extension_single_extension():
    assert Strongest_Extension('Single', ['Extension']) == 'Single.Extension'

def test_strongest_extension_all_lowercase():
    assert Strongest_Extension('Lower', ['abc', 'def']) == 'Lower.abc'

def test_strongest_extension_all_uppercase():
    assert Strongest_Extension('Upper', ['ABC', 'DEF']) == 'Upper.ABC'

def test_strongest_extension_empty_extensions():
    with pytest.raises(IndexError):
        Strongest_Extension('Empty', [])

def test_strongest_extension_complex_names():
    assert Strongest_Extension('Complex', ['MiXeDcAsE', 'aNoThErMiX']) == 'Complex.MiXeDcAsE'

def test_strongest_extension_unicode_characters():
    assert Strongest_Extension('Unicode', ['ABCδ', 'abcΓ']) == 'Unicode.ABCδ'

@pytest.mark.parametrize("class_name,extensions,expected", [
    ('Test1', ['AAA', 'bbb'], 'Test1.AAA'),
    ('Test2', ['aaa', 'BBB'], 'Test2.BBB'),
    ('Test3', ['MiXeD', 'mIxEd'], 'Test3.MiXeD'),
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected
