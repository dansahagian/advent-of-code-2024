import pytest

from settings import DATA_PATH
from solutions.day_01 import (
    diff_of_lists,
    parse_data,
    similarity_of_lists,
)


@pytest.fixture(autouse=True)
def data():
    return parse_data(DATA_PATH / "day_01.txt")


def test_part_1(data):
    assert diff_of_lists(data[0], data[1]) == 1258579


def test_part_2(data):
    assert similarity_of_lists(data[0], data[1]) == 23981443
