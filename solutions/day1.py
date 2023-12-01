from solutions.Puzzle import Puzzle
from typing import List
import re

class Day1(Puzzle):
    day = 1
    num_re = re.compile(r'(\d)')
    calibration_values : List[int] = []
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    def _to_int(self, num: str) -> int:
        try:
            return self.nums.index(num)
        except ValueError:
            return int(num)

    def part1(self) -> int:
        for line in self.data:
            g = self.num_re.findall(line)
            if len(g) < 1:
                raise ValueError(f"No numbers in line: {line}")
            self.calibration_values.append(int(f"{g[0]}{g[-1]}"))
        return sum(self.calibration_values)

    def part2(self) -> int:
        # Reset array
        self.calibration_values = []
        # Regex must use positive lookahead so that "sevenine" returns "79"
        self.num_re = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
        for line in self.data:
            g = self.num_re.findall(line)
            if len(g) < 1:
                raise ValueError(f"No numbers in line: {line}")
            self.calibration_values.append(int(f"{self._to_int(g[0])}{self._to_int(g[-1])}"))
        return sum(self.calibration_values)

