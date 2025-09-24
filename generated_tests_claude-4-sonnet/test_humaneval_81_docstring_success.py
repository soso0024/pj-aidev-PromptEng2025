# Test cases for HumanEval/81
# Generated using Claude API


def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """


   
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade


# Generated test cases:
import pytest

def numerical_letter_grade(grades):
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade

def test_empty_list():
    assert numerical_letter_grade([]) == []

def test_single_grade_a_plus():
    assert numerical_letter_grade([4.0]) == ["A+"]

def test_single_grade_e():
    assert numerical_letter_grade([0.0]) == ["E"]

def test_example_from_docstring():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ["A+", "B", "C-", "C", "A-"]

@pytest.mark.parametrize("gpa,expected", [
    (4.0, "A+"),
    (3.9, "A"),
    (3.8, "A"),
    (3.7, "A-"),
    (3.5, "A-"),
    (3.4, "A-"),
    (3.3, "B+"),
    (3.2, "B+"),
    (3.1, "B+"),
    (3.0, "B"),
    (2.9, "B"),
    (2.8, "B"),
    (2.7, "B-"),
    (2.5, "B-"),
    (2.4, "B-"),
    (2.3, "C+"),
    (2.2, "C+"),
    (2.1, "C+"),
    (2.0, "C"),
    (1.9, "C"),
    (1.8, "C"),
    (1.7, "C-"),
    (1.5, "C-"),
    (1.4, "C-"),
    (1.3, "D+"),
    (1.2, "D+"),
    (1.1, "D+"),
    (1.0, "D"),
    (0.9, "D"),
    (0.8, "D"),
    (0.7, "D-"),
    (0.5, "D-"),
    (0.1, "D-"),
    (0.0, "E")
])
def test_boundary_values(gpa, expected):
    assert numerical_letter_grade([gpa]) == [expected]

def test_all_grades():
    gpas = [4.0, 3.8, 3.5, 3.1, 2.8, 2.5, 2.1, 1.8, 1.5, 1.1, 0.8, 0.5, 0.0]
    expected = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]
    assert numerical_letter_grade(gpas) == expected

def test_negative_grades():
    assert numerical_letter_grade([-1.0, -0.5]) == ["E", "E"]

def test_very_high_grades():
    assert numerical_letter_grade([5.0, 4.5]) == ["A", "A"]

def test_decimal_precision():
    assert numerical_letter_grade([3.70001, 3.69999]) == ["A", "A-"]
    assert numerical_letter_grade([3.30001, 3.29999]) == ["A-", "B+"]

def test_mixed_grades():
    gpas = [4.0, 0.0, 2.5, 3.8, 1.2, 0.9]
    expected = ["A+", "E", "B-", "A", "D+", "D"]
    assert numerical_letter_grade(gpas) == expected

def test_duplicate_grades():
    assert numerical_letter_grade([3.5, 3.5, 3.5]) == ["A-", "A-", "A-"]

def test_float_precision_edge_cases():
    assert numerical_letter_grade([3.7000000001]) == ["A"]
    assert numerical_letter_grade([3.6999999999]) == ["A-"]