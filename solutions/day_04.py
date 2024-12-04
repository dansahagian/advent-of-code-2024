from settings import DATA_PATH


def parse_data() -> list[list[str]]:
    with open(DATA_PATH / "day_04.txt", "r") as f:
        data = [list(row) for row in f.readlines()]
    return data


def search_right(grid: list[list[str]], row_index: int, col_index: int) -> int:
    r, c = row_index, col_index
    try:
        word = "".join([grid[r][c + x] for x in range(0, 4)])
        if word == "XMAS" or word == "SAMX":
            return 1
    except IndexError:
        return 0
    return 0


def search_down(grid: list[list[str]], row_index: int, col_index: int) -> int:
    r, c = row_index, col_index
    try:
        word = "".join([grid[r + x][c] for x in range(0, 4)])
        if word == "XMAS" or word == "SAMX":
            return 1
    except IndexError:
        return 0
    return 0


def search_right_diagonal(grid: list[list[str]], row_index: int, col_index: int) -> int:
    r, c = row_index, col_index
    try:
        word = "".join([grid[r + x][c + x] for x in range(0, 4)])
        if word == "XMAS" or word == "SAMX":
            return 1
    except IndexError:
        return 0
    return 0


def search_left_diagonal(grid: list[list[str]], row_index: int, col_index: int) -> int:
    r, c = row_index, col_index
    if c < 3:
        return 0
    try:
        word = "".join([grid[r + x][c - x] for x in range(0, 4)])
        if word == "XMAS" or word == "SAMX":
            return 1
    except IndexError:
        return 0
    return 0


def search_for_x_mas(grid: list[list[str]], row_index: int, col_index: int) -> int:
    r, c = row_index, col_index
    try:
        rd = "".join([grid[r + x][c + x] for x in range(0, 3)])
        ld = "".join([grid[r + x][c + 2 - x] for x in range(0, 3)])
        if (rd == "MAS" or rd == "SAM") and (ld == "MAS" or ld == "SAM"):
            return 1
    except IndexError:
        return 0
    return 0


def search_from_root(grid: list[list[str]], row_index: int, col_index: int) -> int:
    right = search_right(grid, row_index, col_index)
    down = search_down(grid, row_index, col_index)
    right_diagonal = search_right_diagonal(grid, row_index, col_index)
    left_diagonal = search_left_diagonal(grid, row_index, col_index)

    return right + down + right_diagonal + left_diagonal


def word_find() -> tuple[int, int]:
    grid = parse_data()
    count_xmas = 0
    count_x_mas = 0
    for row_index, row in enumerate(grid):
        for col_index, letter in enumerate(row):
            if letter in {"X", "S"}:
                count_xmas += search_from_root(grid, row_index, col_index)
            if letter in {"S", "M"}:
                count_x_mas += search_for_x_mas(grid, row_index, col_index)
    return count_xmas, count_x_mas


if __name__ == "__main__":
    print(word_find())
