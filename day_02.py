from copy import deepcopy


def analyze_levels(previous: int, current: int) -> tuple[bool, int]:
    diff = current - previous
    if diff == 0 or diff < -3 or diff > 3:
        return False, 0

    if 1 <= diff <= 3:
        return True, 1

    if -3 <= diff <= -1:
        return True, -1


def check_safety(levels: list[int]) -> bool:
    previous = levels[0]
    trend = None

    for current in levels[1:]:
        safe, tmp_trend = analyze_levels(previous, current)
        if not safe:
            return False
        if trend and tmp_trend != trend:
            return False
        else:
            trend = tmp_trend
        previous = current

    return True


def check_safety_with_dampening(levels: list[int]) -> bool:
    for i in range(len(levels)):
        dampened_levels = deepcopy(levels)
        dampened_levels.pop(i)
        if check_safety(dampened_levels):
            return True
    return False


def main():
    number_safe = 0
    number_safe_with_dampening = 0
    with open("inputs/day_02.txt", "r") as f:
        for report in f:
            levels = [int(x) for x in report.strip().split()]
            if check_safety(levels):
                number_safe += 1
            elif check_safety_with_dampening(levels):
                number_safe_with_dampening += 1

    print(f"safe reports: {number_safe}")
    print(f"safe reports with dampening: {number_safe_with_dampening}")
    print(f"total safe: {number_safe_with_dampening + number_safe}")


if __name__ == "__main__":
    main()
