from solutions.Puzzle import Puzzle
from typing import List


class Day9(Puzzle):
    day = 9

    def __init__(self, data=None):
        super().__init__(data)
        self.data = [[int(x) for x in line.split(" ")] for line in self.data]

    @staticmethod
    def extrapolate(line: List[int]):
        diffs = [y - x for x, y in zip(line, line[1:])]
        return line[-1] + Day9.extrapolate(diffs) if diffs else 0

    def part1(self) -> int:
        return sum([Day9.extrapolate(line) for line in self.data])

    def part2(self) -> int:
        return sum([Day9.extrapolate(line[::-1]) for line in self.data])
