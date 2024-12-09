from settings import DATA_PATH


def parse_data():
    data = {}
    with open(DATA_PATH / "day_08.txt", "r") as f:
        for i, row in enumerate(f.readlines()):
            for j, item in enumerate(list(row.strip())):
                if item != ".":
                    if item in data:
                        data[item].append((i, j))
                    else:
                        data[item] = [(i, j)]
    return data, i, j


def check_antinode(a1: tuple[int, int], x_bound: int, y_bound: int) -> bool:
    x, y = a1
    if x < 0 or x > x_bound:
        return False
    if y < 0 or y > y_bound:
        return False

    return True


def get_antinodes(
    p1: tuple[int, int],
    p2: tuple[int, int],
    x_bound: int,
    y_bound: int,
) -> set[tuple[int, int]]:
    diff = (p1[0] - p2[0], p1[1] - p2[1])
    antinodes = ((p1[0] + diff[0], p1[1] + diff[1]), (p2[0] - diff[0], p2[1] - diff[1]))

    return {x for x in antinodes if check_antinode(x, x_bound, y_bound)}


def get_harmonic_antinodes(
    p1: tuple[int, int],
    p2: tuple[int, int],
    x_bound: int,
    y_bound: int,
) -> set[tuple[int, int]]:
    antinodes = {p1}

    diff = (p1[0] - p2[0], p1[1] - p2[1])
    a = (p1[0] + diff[0], p1[1] + diff[1])

    while check_antinode(a, x_bound, y_bound):
        antinodes.add(a)
        a = (a[0] + diff[0], a[1] + diff[1])

    b = (p1[0] - diff[0], p1[1] - diff[1])
    while check_antinode(b, x_bound, y_bound):
        antinodes.add(b)
        b = (b[0] - diff[0], b[1] - diff[1])

    return antinodes


def count_antinodes() -> tuple[int, int]:
    antennae, x_bound, y_bound = parse_data()
    antinodes = set()
    harmonic_antinodes = set()

    for key, vals in antennae.items():
        num_of_values = len(vals)
        for i in range(num_of_values - 1):
            for j in range(i + 1, num_of_values):
                p1, p2 = vals[i], vals[j]
                for a in get_antinodes(p1, p2, x_bound, y_bound):
                    antinodes.add(a)
                for b in get_harmonic_antinodes(p1, p2, x_bound, y_bound):
                    harmonic_antinodes.add(b)

    return len(antinodes), len(harmonic_antinodes)


if __name__ == "__main__":
    print(count_antinodes())
