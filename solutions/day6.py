from solutions.Puzzle import Puzzle
import re

numbers = re.compile(r"(\d+)")


class Day6(Puzzle):
    day = 6

    def __init__(self, data=None):
        super().__init__(data)
        self.times = [int(x.group(0)) for x in numbers.finditer(self.data[0])]
        self.distances = [int(x.group(0)) for x in numbers.finditer(self.data[1])]

    @staticmethod
    def min(time, distance) -> int:
        for button_hold in range(0, time):
            if (button_hold * (time - button_hold)) > distance:
                return button_hold
        return 1

    @staticmethod
    def max(time, distance) -> int:
        for button_hold in range(time - 1, 1, -1):
            if (button_hold * (time - button_hold)) > distance:
                return button_hold
        return time - 1

    def part1(self) -> int:
        margins_of_error = []
        for race in zip(self.times, self.distances):
            min_hold = self.min(race[0], race[1])
            max_hold = self.max(race[0], race[1])
            margins_of_error.append(max_hold - min_hold + 1)
        res = 1
        for x in margins_of_error:
            res *= x
        return res

    def part2(self) -> int:
        time = int("".join(str(x) for x in self.times))
        distance = int("".join(str(x) for x in self.distances))
        min_hold = self.min(time, distance)
        max_hold = self.max(time, distance)
        return max_hold - min_hold + 1
