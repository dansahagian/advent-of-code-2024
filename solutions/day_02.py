from copy import deepcopy

from settings import DATA_PATH


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


def get_safe_counts(reports: list[list]) -> tuple[int, int]:
    safe_count = 0
    safe_with_dampening_count = 0

    for report in reports:
        if check_safety(report):
            safe_count += 1
        elif check_safety_with_dampening(report):
            safe_with_dampening_count += 1

    return safe_count, safe_with_dampening_count


def parse_data():
    with open(DATA_PATH / "day_02.txt", "r") as data:
        reports = [[int(x) for x in row.strip().split()] for row in data]
    return reports


def main():
    reports = parse_data()
    safe_count, safe_with_dampening_count = get_safe_counts(reports)

    print(f"safe reports: {safe_count}")
    print(f"safe reports with dampening: {safe_with_dampening_count}")
    print(f"total safe: {safe_with_dampening_count + safe_count}")


if __name__ == "__main__":
    main()
