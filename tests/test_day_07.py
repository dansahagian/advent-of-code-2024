from solutions.day_07 import (
    get_three_op_calibration_result,
    get_two_op_calibration_result,
)


def test_part_1():
    assert get_two_op_calibration_result() == 1399219271639


def test_part_2():
    assert get_three_op_calibration_result() == 275791737999003
