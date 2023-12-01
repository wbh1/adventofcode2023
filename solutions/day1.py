from solutions.Puzzle import Puzzle
from typing import List
import re


class Day1(Puzzle):
    day = 1
    num_re = re.compile(r"(\d)")
    calibration_values: List[int] = []
    nums = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    def _to_int(self, num: str) -> int:
        try:
            return self.nums.index(num)
        except ValueError:
            return int(num)

    def _parse_line(self, line) -> int:
        g = self.num_re.findall(line)
        if len(g) < 1:
            raise ValueError(f"No numbers in line: {line}")
        return int(f"{self._to_int(g[0])}{self._to_int(g[-1])}")

    def part1(self) -> int:
        self.calibration_values = [self._parse_line(line) for line in self.data]
        return sum(self.calibration_values)

    def part2(self) -> int:
        # Regex must use positive lookahead so that "sevenine" returns "79"
        self.num_re = re.compile(
            r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
        )
        self.calibration_values = [self._parse_line(line) for line in self.data]
        return sum(self.calibration_values)
