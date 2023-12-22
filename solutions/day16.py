from solutions.Puzzle import Puzzle
from typing import Tuple
import sys

sys.setrecursionlimit(10000)


class Day16(Puzzle):
    day = 16

    def __init__(self, data=None):
        super().__init__(data)
        self.energized = set()
        self.moves = set()

    @staticmethod
    def travel(direction: str) -> Tuple[int, int]:
        if direction == "U":
            return (0, -1)
        elif direction == "D":
            return (0, 1)
        elif direction == "L":
            return (-1, 0)
        elif direction == "R":
            return (1, 0)
        else:
            raise ValueError("Unknown direction:", direction)

    def beam(self, coordinate: Tuple[int, int], direction: str):
        (x, y) = coordinate
        while x >= 0 and y >= 0:
            try:
                value = self.data[y][x]
                self.energized.add(coordinate)
                if (direction, x, y) in self.moves:
                    return
                else:
                    self.moves.add((direction, x, y))
                if value == ".":
                    coordinate = tuple(
                        map(sum, zip(coordinate, self.travel(direction)))  # type: ignore
                    )
                elif value == r"/":
                    if direction == "U":
                        direction = "R"
                    elif direction == "D":
                        direction = "L"
                    elif direction == "R":
                        direction = "U"
                    elif direction == "L":
                        direction = "D"
                    coordinate = tuple(
                        map(sum, zip(coordinate, self.travel(direction)))  # type: ignore
                    )
                elif value == "\\":
                    if direction == "U":
                        direction = "L"
                    elif direction == "D":
                        direction = "R"
                    elif direction == "R":
                        direction = "D"
                    elif direction == "L":
                        direction = "U"
                    coordinate = tuple(
                        map(sum, zip(coordinate, self.travel(direction)))  # type: ignore
                    )
                elif value == r"-":
                    if direction == "U" or direction == "D":
                        direction = "R"
                        self.beam(
                            tuple(map(sum, zip(coordinate, self.travel("L")))),  # type: ignore
                            direction="L",
                        )
                        coordinate = tuple(
                            map(sum, zip(coordinate, self.travel(direction)))  # type: ignore
                        )
                    else:
                        coordinate = tuple(
                            map(sum, zip(coordinate, self.travel(direction)))  # type: ignore
                        )
                elif value == r"|":
                    if direction == "R" or direction == "L":
                        direction = "U"
                        self.beam(
                            tuple(map(sum, zip(coordinate, self.travel("D")))),  # type: ignore
                            direction="D",
                        )
                        coordinate = tuple(
                            map(sum, zip(coordinate, self.travel(direction)))  # type: ignore
                        )
                    else:
                        coordinate = tuple(
                            map(sum, zip(coordinate, self.travel(direction)))  # type: ignore
                        )
            except IndexError:
                return
            finally:
                (x, y) = coordinate

    def part1(self) -> int:
        coordinate = (0, 0)
        self.beam(coordinate, "R")
        return len(self.energized)

    def part2(self) -> int:
        res = len(self.energized)
        for y in range(0, len(self.data)):
            # left side y coordinates
            coordinate = (0, y)
            self.energized.clear()
            self.moves.clear()
            self.beam(coordinate, "R")
            res = max(res, len(self.energized))

            # right side y-coordinates
            coordinate = (len(self.data[0]) - 1, y)
            self.energized.clear()
            self.moves.clear()
            self.beam(coordinate, "L")
            res = max(res, len(self.energized))
        for x in range(0, len(self.data[0])):
            # top row coordinates
            coordinate = (x, 0)
            self.energized.clear()
            self.moves.clear()
            self.beam(coordinate, "D")
            res = max(res, len(self.energized))

            # bottom row coordinates
            coordinate = (x, len(self.data) - 1)
            self.energized.clear()
            self.moves.clear()
            self.beam(coordinate, "U")
            res = max(res, len(self.energized))

        return max(res, len(self.energized))
