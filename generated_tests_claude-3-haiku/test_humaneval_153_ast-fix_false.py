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
    if not extensions:
        raise IndexError
    strong = max(extensions, key=lambda s: len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()]))
    return f"{class_name}.{strong}"

def test_strongest_extension_normal_case():
    class_name = "MyClass"
    extensions = ["PY", "Py", "pY", "py"]
    assert Strongest_Extension(class_name, extensions) == "MyClass.PY"

def test_strongest_extension_all_uppercase():
    class_name = "AnotherClass"
    extensions = ["CPP", "H", "HPP"]
    assert Strongest_Extension(class_name, extensions) == "AnotherClass.CPP"

def test_strongest_extension_all_lowercase():
    class_name = "LowerClass"
    extensions = ["txt", "md", "py"]
    assert Strongest_Extension(class_name, extensions) == "LowerClass.py"

def test_strongest_extension_mixed_case():
    class_name = "MixedClass"
    extensions = ["jAVA", "cSS", "hTML"]
    assert Strongest_Extension(class_name, extensions) == "MixedClass.jAVA"

def test_strongest_extension_single_extension():
    class_name = "SingleClass"
    extensions = ["SINGLE"]
    assert Strongest_Extension(class_name, extensions) == "SingleClass.SINGLE"

def test_strongest_extension_empty_extensions():
    class_name = "EmptyClass"
    extensions = []
    with pytest.raises(IndexError):
        Strongest_Extension(class_name, extensions)

@pytest.mark.parametrize("class_name,extensions,expected", [
    ("TestClass", ["PY", "Py", "pY", "py"], "TestClass.PY"),
    ("AnotherTest", ["CPP", "H", "HPP"], "AnotherTest.CPP"),
    ("LowerTest", ["txt", "md", "py"], "LowerTest.py"),
    ("MixedTest", ["jAVA", "cSS", "hTML"], "MixedTest.jAVA"),
    ("SingleTest", ["SINGLE"], "SingleTest.SINGLE"),
    ("EmptyTest", [], IndexError)
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    if expected == IndexError:
        with pytest.raises(IndexError):
            Strongest_Extension(class_name, extensions)
    else:
        assert Strongest_Extension(class_name, extensions) == expected