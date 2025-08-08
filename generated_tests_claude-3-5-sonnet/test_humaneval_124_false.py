# Test cases for HumanEval/124
# Generated using Claude API


def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """

    try:
        date = date.strip()
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        if month < 1 or month > 12:
            return False
        if month in [1,3,5,7,8,10,12] and day < 1 or day > 31:
            return False
        if month in [4,6,9,11] and day < 1 or day > 30:
            return False
        if month == 2 and day < 1 or day > 29:
            return False
    except:
        return False

    return True


# Generated test cases:
import pytest

@pytest.mark.parametrize("date,expected", [
    ("01-01-2023", True),
    ("12-31-2023", True),
    ("02-29-2024", True),
    ("04-30-2023", True),
    ("13-01-2023", False),
    ("00-01-2023", False),
    ("01-32-2023", False),
    ("02-30-2023", False),
    ("04-31-2023", False),
    ("a-01-2023", False),
    ("01-b-2023", False),
    ("01-01-abcd", False),
    ("01--1-2023", False),
    ("", False),
    ("01-01", False),
    ("01-01-2023-4", False),
    (" 01-01-2023 ", True),
    ("01-01-2023\n", True),
    ("\t01-01-2023\t", True),
    ("not-a-date", False),
    ("2023-01-01", False),
    ("01/01/2023", False),
    ("01.01.2023", False)
])
def test_valid_date_parametrized(date, expected):
    assert valid_date(date) == expected

def test_valid_date_none_input():
    assert valid_date(None) == False

def test_valid_date_non_string_input():
    assert valid_date(123) == False
    assert valid_date(1.23) == False
    assert valid_date([1,2,3]) == False
    assert valid_date({'date': '01-01-2023'}) == False

def test_valid_date_months_with_31_days():
    for month in [1, 3, 5, 7, 8, 10, 12]:
        assert valid_date(f"{month:02d}-31-2023") == True
        assert valid_date(f"{month:02d}-32-2023") == False

def test_valid_date_months_with_30_days():
    for month in [4, 6, 9, 11]:
        assert valid_date(f"{month:02d}-30-2023") == True
        assert valid_date(f"{month:02d}-31-2023") == False

def test_valid_date_february():
    assert valid_date("02-28-2023") == True
    assert valid_date("02-29-2024") == True
    assert valid_date("02-30-2023") == False