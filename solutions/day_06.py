from settings import DATA_PATH


class FloorMap:
    def __init__(self):
        self.directions: set = {"^", "v", ">", "<"}
        self.floor_map: list = []
        self.guard_position: tuple[int, int] = (0, 0)
        self.guard_direction: str = "^"
        self.positions: list = []

        self.path: dict = {}

        self.t_bound: int = 0
        self.l_bound: int = 0
        self.r_bound: int = 0
        self.b_bound: int = 0

        self.move: str = "Yes"

        self.parse_data()

    def parse_data(self) -> None:
        row = 0
        with open(DATA_PATH / "day_06.txt", "r") as f:
            for line in f.readlines():
                data = list(line.strip())
                self.floor_map.append(data)
                for col, d in enumerate(data):
                    if d in self.directions:
                        self.guard_position = (row, col)
                        self.positions.append(self.guard_position)
                        self.guard_direction = d
                        self.path[f"{row}|{col}|{self.guard_direction}"] = 1
                row += 1
            self.r_bound = len(data) - 1
            self.b_bound = len(self.floor_map) - 1

    def get_next_position(self) -> tuple[int, int]:
        row, col = self.guard_position
        match self.guard_direction:
            case "^":
                return row - 1, col
            case "v":
                return row + 1, col
            case ">":
                return row, col + 1
            case "<":
                return row, col - 1

    def turn_90_degrees(self) -> None:
        match self.guard_direction:
            case "^":
                self.guard_direction = ">"
            case "v":
                self.guard_direction = "<"
            case ">":
                self.guard_direction = "v"
            case "<":
                self.guard_direction = "^"

    def make_one_move(self) -> None:
        r, c = self.get_next_position()
        if r < self.t_bound or r > self.b_bound or c < self.l_bound or c > self.r_bound:
            self.move = "Off Map"
            return
        val = self.floor_map[r][c]

        if val == "#":
            self.turn_90_degrees()
        else:
            n = self.path.get(f"{r}|{c}|{self.guard_direction}", 1)
            self.path[f"{r}|{c}|{self.guard_direction}"] = n + 1
            if self.path[f"{r}|{c}|{self.guard_direction}"] > 2:
                self.move = "Loop"
                return
            self.guard_position = (r, c)
            self.positions.append(self.guard_position)

        return

    def walk(self):
        while self.move == "Yes":
            self.make_one_move()


def count_guard_positions() -> int:
    fm = FloorMap()
    fm.walk()
    answer = len(set(fm.positions))
    print(answer)
    return answer


def count_obstruction_loops() -> int:
    obstruction_points = 0
    fm = FloorMap()
    fm.walk()
    for pos in set(fm.positions):
        row, col = pos
        fm = FloorMap()
        if fm.guard_position != (row, col):
            fm.floor_map[row][col] = "#"
            fm.walk()
            if fm.move == "Loop":
                obstruction_points += 1
    print(obstruction_points)
    return obstruction_points


if __name__ == "__main__":
    count_guard_positions()
    count_obstruction_loops()
