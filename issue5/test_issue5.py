from what_is_year import what_is_year_now
import pytest
from unittest.mock import patch


@pytest.fixture
def mock_open():
    with patch("what_is_year.urllib.request.urlopen") as mock_open:
        yield mock_open


def test_common1(mock_open):
    cur_date = '{"currentDateTime": "2023-03-01"}'
    mock_open.return_value.__enter__.return_value.read.return_value = cur_date
    year = what_is_year_now()
    assert year == 2023


def test_common2(mock_open):
    cur_date = '{"currentDateTime": "01.03.2019"}'
    mock_open.return_value.__enter__.return_value.read.return_value = cur_date
    year = what_is_year_now()
    assert year == 2019


def test_exception(mock_open):
    cur_date = '{"currentDateTime": "01@03@2019"}'
    mock_open.return_value.__enter__.return_value.read.return_value = cur_date
    with pytest.raises(ValueError):
        what_is_year_now()
