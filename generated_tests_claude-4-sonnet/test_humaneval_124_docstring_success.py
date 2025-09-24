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

def valid_date(date):
    try:
        date = date.strip()
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        if month < 1 or month > 12:
            return False
        if month in [1,3,5,7,8,10,12] and (day < 1 or day > 31):
            return False
        if month in [4,6,9,11] and (day < 1 or day > 30):
            return False
        if month == 2 and (day < 1 or day > 29):
            return False
    except:
        return False
    return True

@pytest.mark.parametrize("date_str,expected", [
    ("03-11-2000", True),
    ("15-01-2012", False),
    ("04-0-2040", False),
    ("06-04-2020", True),
    ("06/04/2020", False),
    ("", False),
    ("01-01-2000", True),
    ("12-31-2000", True),
    ("13-01-2000", False),
    ("00-01-2000", False),
    ("01-32-2000", False),
    ("01-00-2000", False),
    ("02-29-2000", True),
    ("02-30-2000", False),
    ("04-31-2000", False),
    ("04-30-2000", True),
    ("06-31-2000", False),
    ("06-30-2000", True),
    ("09-31-2000", False),
    ("09-30-2000", True),
    ("11-31-2000", False),
    ("11-30-2000", True),
    ("01-31-2000", True),
    ("03-31-2000", True),
    ("05-31-2000", True),
    ("07-31-2000", True),
    ("08-31-2000", True),
    ("10-31-2000", True),
    ("12-31-2000", True),
    ("1-1-2000", True),
    ("01-1-2000", True),
    ("1-01-2000", True),
    ("abc-def-ghi", False),
    ("01-abc-2000", False),
    ("abc-01-2000", False),
    ("01-01-abc", False),
    ("01-01", False),
    ("01", False),
    ("01-01-2000-extra", False),
    ("2000-01-01", False),
    ("01.01.2000", False),
    ("01 01 2000", False),
    (" 01-01-2000 ", True),
    ("  03-11-2000  ", True),
])
def test_valid_date(date_str, expected):
    assert valid_date(date_str) == expected

def test_valid_date_empty_string():
    assert valid_date("") == False

def test_valid_date_none_input():
    assert valid_date(None) == False

def test_valid_date_integer_input():
    assert valid_date(123) == False

def test_valid_date_february_edge_cases():
    assert valid_date("02-01-2000") == True
    assert valid_date("02-28-2000") == True
    assert valid_date("02-29-2000") == True
    assert valid_date("02-30-2000") == False
    assert valid_date("02-31-2000") == False

def test_valid_date_month_boundaries():
    assert valid_date("01-15-2000") == True
    assert valid_date("12-15-2000") == True
    assert valid_date("00-15-2000") == False
    assert valid_date("13-15-2000") == False

def test_valid_date_day_boundaries_31_day_months():
    for month in ["01", "03", "05", "07", "08", "10", "12"]:
        assert valid_date(f"{month}-01-2000") == True
        assert valid_date(f"{month}-31-2000") == True
        assert valid_date(f"{month}-32-2000") == False
        assert valid_date(f"{month}-00-2000") == False

def test_valid_date_day_boundaries_30_day_months():
    for month in ["04", "06", "09", "11"]:
        assert valid_date(f"{month}-01-2000") == True
        assert valid_date(f"{month}-30-2000") == True
        assert valid_date(f"{month}-31-2000") == False
        assert valid_date(f"{month}-00-2000") == False