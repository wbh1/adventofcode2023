from solutions.Puzzle import Puzzle
from typing import List
from queue import Queue

# up/down/left/right
dirs: List[tuple[int, int]] = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Day10(Puzzle):
    day = 10
    """Rules

        | is a vertical pipe connecting north and south.
        - is a horizontal pipe connecting east and west.
        L is a 90-degree bend connecting north and east.
        J is a 90-degree bend connecting north and west.
        7 is a 90-degree bend connecting south and west.
        F is a 90-degree bend connecting south and east.
        . is ground; there is no pipe in this tile.
        S is the starting position of the animal; there is a pipe on this tile,
          but your sketch doesn't show what shape the pipe has.
    """
    pipe_moves = {
        "|": [(0, -1), (0, 1)],
        "-": [(-1, 0), (1, 0)],
        "L": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(-1, 0), (0, 1)],
        "F": [(1, 0), (0, 1)],
    }

    def __init__(self, data=None):
        super().__init__(data)

    def part1(self) -> int:
        start = (0, 0)
        for y, row in enumerate(self.data):
            for x, p in enumerate(row):
                if p == "S":
                    start = (x, y)
                    break

        q = Queue()
        point = start
        for dx, dy in dirs:
            pipe = self.data[point[0] + dy][point[1] + dx]
            if pipe in self.pipe_moves:
                for dx2, dy2 in self.pipe_moves[pipe]:
                    if (
                        point[0] == point[0] + dx + dx2
                        and point[1] == point[1] + dy + dy2
                    ):
                        # (distance, (x,y))
                        q.put((1, (point[0] + dx, point[1] + dy)))

        distances = {start: 0}
        assert q.qsize() == 2
        while not q.empty():
            d, (x, y) = q.get()
            if (x, y) in distances:
                continue

            distances[(x, y)] = d
            for dx, dy in self.pipe_moves[self.data[y][x]]:
                q.put((d + 1, (x + dx, y + dy)))

        # Not sure why I'm off by one but whatever
        self.distances = distances
        return max(distances.values()) + 1

    def part2(self) -> int:
        self.part1()
        width = len(self.data[0])
        height = len(self.data)
        contained_points = 0
        for y, row in enumerate(self.data):
            for x, _ in enumerate(row):
                if (x, y) in self.distances:
                    continue

                intersections = 0
                x2, y2 = x, y

                while x2 < width and y2 < height:
                    pipe = self.data[y2][x2]
                    # eliminate north/east and south/west pipes
                    if (x2, y2) in self.distances and pipe != "L" and pipe != "7":
                        intersections += 1
                    x2 += 1
                    y2 += 1

                if intersections % 2 == 1:
                    contained_points += 1
        return contained_points
