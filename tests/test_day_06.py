from solutions.day_06 import count_guard_positions, count_obstruction_loops


def test_part_1():
    assert count_guard_positions() == 5312


def test_part_2():
    assert count_obstruction_loops() == 1748
