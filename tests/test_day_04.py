import pytest

from solutions.day_04 import parse_data, word_find_part_1


@pytest.fixture
def grid():
    return parse_data()


def test_part_1(grid):
    assert word_find_part_1(grid) == 2536
