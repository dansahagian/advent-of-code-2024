import pytest

from solutions.day_02 import get_safe_counts, parse_data


@pytest.fixture(autouse=True)
def data():
    return parse_data()


def test_solution(data):
    safe_count, safe_with_dampening_count = get_safe_counts(data)
    assert safe_count == 486
    assert safe_count + safe_with_dampening_count == 540
