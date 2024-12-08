from settings import DATA_PATH


def parse_data() -> list:
    data = []
    with open(DATA_PATH / "day_07.txt", "r") as f:
        for line in f.readlines():
            row = line.strip().split(": ")
            data.append([int(row[0]), [int(x) for x in row[1].split(" ")]])

    return data


def check_two_op_val(row: list[int, list[int]]) -> int:
    test_val, inputs = row
    results = [[inputs[0]]]
    for i in range(len(inputs) - 1):
        level = []
        for n in results[i]:
            level.append(n * inputs[i + 1])
            level.append(n + inputs[i + 1])
        results.append(level)
    if test_val in results[-1]:
        return test_val
    return 0


def check_three_op_val(row: list[int, list[int]]) -> int:
    test_val, inputs = row
    results = [[inputs[0]]]
    for i in range(len(inputs) - 1):
        level = []
        for n in results[i]:
            level.append(n * inputs[i + 1])
            level.append(n + inputs[i + 1])
            level.append(int(str(n) + str(inputs[i + 1])))
        results.append(level)
    if test_val in results[-1]:
        return test_val
    return 0


def get_two_op_calibration_result() -> int:
    data = parse_data()
    total = 0
    for row in data:
        if val := check_two_op_val(row):
            total += val
    return total


def get_three_op_calibration_result() -> int:
    data = parse_data()
    total = 0
    for row in data:
        if val := check_three_op_val(row):
            total += val
    return total


if __name__ == "__main__":
    print(get_two_op_calibration_result())
    print(get_three_op_calibration_result())
