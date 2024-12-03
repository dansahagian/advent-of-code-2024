from settings import DATA_PATH


def read_raw_data() -> str:
    with open(DATA_PATH / "day_03.txt", "r") as f:
        data = f.read()
    return data


def parse_data() -> list[list[str]]:
    with open(DATA_PATH / "day_03.txt", "r") as f:
        data = f.read()
    return [d.split(")")[0].split(",") for d in data.split("mul(")]


def validated_pair_product(pair: list[str]) -> int:
    if len(pair) != 2:
        return 0
    try:
        return int(pair[0]) * int(pair[1])
    except ValueError:
        return 0


def sum_of_multiplications(parsed_data: list[list[str]]) -> int:
    total = 0
    for pair in parsed_data:
        total += validated_pair_product(pair)
    return total


def find_enabled_ranges(raw_data: str) -> list[list[int]]:
    changes = [0]
    cursor = 0
    instruction = "don't()"
    while cursor != -1:
        cursor = raw_data.find(instruction, cursor + 1)
        changes.append(cursor)
        instruction = "do()" if instruction == "don't()" else "don't()"

    changes[-1] = len(raw_data)
    return [changes[i : i + 2] for i in range(0, len(changes), 2)]


def is_mul_enabled(enabled_ranges: list[list[int]], cursor: int) -> bool:
    for enabled_range in enabled_ranges:
        if enabled_range[0] <= cursor <= enabled_range[1]:
            return True
    return False


def sum_of_enabled_multiplications(raw_data: str, parsed_data: list[list[str]]):
    enabled_ranges = find_enabled_ranges(raw_data)
    total = 0
    cursor = 0
    for pair in parsed_data:
        if product := validated_pair_product(pair):
            mul = f"mul({pair[0]},{pair[1]})"
            cursor = raw_data.find(mul, cursor)
            if is_mul_enabled(enabled_ranges, cursor):
                total += product
    return total


def main():
    parsed_data = parse_data()
    raw_data = read_raw_data()

    som = sum_of_multiplications(parsed_data)
    soem = sum_of_enabled_multiplications(raw_data, parsed_data)
    print(som)
    print(soem)


if __name__ == "__main__":
    main()
