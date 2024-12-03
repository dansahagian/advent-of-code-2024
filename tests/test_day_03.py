import pytest

from solutions.day_03 import (
    parse_data,
    read_raw_data,
    sum_of_enabled_multiplications,
    sum_of_multiplications,
)


@pytest.fixture
def parsed_data():
    return parse_data()


@pytest.fixture
def raw_data():
    return read_raw_data()


def test_part_1(parsed_data):
    assert sum_of_multiplications(parsed_data) == 174336360


def test_part_2(raw_data, parsed_data):
    assert sum_of_enabled_multiplications(raw_data, parsed_data) == 88802350
