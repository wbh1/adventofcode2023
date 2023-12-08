from solutions.Puzzle import Puzzle
import re
import math
from typing import Callable

regex = re.compile(r"(?P<element>\w+) = \((?P<left>\w+), (?P<right>\w+)\)")


class Day8(Puzzle):
    day = 8

    def __init__(self, data=None):
        super().__init__(data)
        self.directions = self.data[0]
        self.elements = {}
        for d in self.data[2:]:
            m = regex.match(d)
            if m is None:
                raise ValueError(f"Couldn't regex match this line: '{d}'")
            self.elements[m.group("element")] = {
                "L": m.group("left"),
                "R": m.group("right"),
            }

    def travel(
        self, start: str, direction_index: int, end: Callable[[str], bool]
    ) -> int:
        steps = 0
        while not end(start):
            steps += 1
            direction = self.directions[direction_index % len(self.directions)]
            start = self.elements[start][direction]
            direction_index += 1
        return steps

    def part1(self) -> int:
        return self.travel("AAA", 0, lambda x: x == "ZZZ")

    def part2(self) -> int:
        starts = filter(lambda x: x[2] == "A", self.elements.keys())
        lcm = 1
        for s in starts:
            lcm = math.lcm(lcm, self.travel(s, 0, lambda x: x[2] == "Z"))
        return lcm
