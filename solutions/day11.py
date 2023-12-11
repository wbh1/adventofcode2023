from solutions.Puzzle import Puzzle
from typing import List, Dict
from itertools import combinations


class Day11(Puzzle):
    day = 11

    def __init__(self, data=None):
        super().__init__(data)
        self.mapped_universe: Dict[tuple[int, int], str] = {}

    def expand(self, adjustment=2):
        self.mapped_universe.clear()
        adj_x = 0
        adj_y = 0

        new_universe_ys: List[int] = []
        new_universe_xs: List[List[int]] = [[] for row in self.data]

        # For each row, add its Y value to the list
        # If the row is all empty, increase the space between
        # this row and the next row by "adjustment" minus 1 (since we count this row still).
        for ri, row in enumerate(self.data):
            new_universe_ys.append(ri + adj_y)
            if all(c == "." for c in row):
                adj_y += adjustment - 1

        # For each column, add its X values for each row to the list.
        # If the column is all empty, increase the space between
        # this row and the next X value by the adjustment
        for col in range(0, len(self.data[0])):
            if all(row[col] == "." for row in self.data):
                adj_x += adjustment - 1
            # For each row, append the X value of the coordinate
            # to a list of the X values for the row
            for ri in range(0, len(self.data)):
                new_universe_xs[ri].append(col + adj_x)

        # Finally, map the universe by creating cartesian coordinates
        # through combining the x and y values
        # Each Y value (row) will have multiple X values (columns)
        # to iterate through.
        # Since we didn't add or remove any non-empty space from the original map
        # we can still use indices to get the contents of a point.
        for ri, (y, xs) in enumerate(zip(new_universe_ys, new_universe_xs)):
            for ci, x in enumerate(xs):
                self.mapped_universe[(x, y)] = self.data[ri][ci]

    def galaxies(self) -> List[tuple[int, int]]:
        galaxies: List[tuple[int, int]] = []
        for point, value in self.mapped_universe.items():
            if value == "#":
                galaxies.append(point)
        return galaxies

    def part1(self) -> int:
        self.expand()
        distances: List[int] = []
        for (x1, y1), (x2, y2) in combinations(self.galaxies(), 2):
            distances.append(abs(x2 - x1) + abs(y2 - y1))

        return sum(distances)

    def part2(self, adjustment=1000000) -> int:
        self.expand(adjustment)
        distances: List[int] = []
        for (x1, y1), (x2, y2) in combinations(self.galaxies(), 2):
            distances.append(abs(x2 - x1) + abs(y2 - y1))

        return sum(distances)
