from solutions.Puzzle import Puzzle
import re
from collections import defaultdict
from typing import List


class Game:
    p = re.compile(r"((?P<blue>\d+) blue)?((?P<green>\d+) green)?((?P<red>\d+) red)?")

    def __init__(self, id: int, line: str):
        self.id = id
        self.rounds = []
        for r in line.split(";"):
            result = defaultdict(lambda: 0)
            matches = self.p.finditer(r)
            # Because each match will only have a number > 0 for one color,
            # and I don't want to keep experimenting with my regex,
            # iterate through each match and add its number to a dict
            for m in matches:
                for color, value in m.groupdict(0).items():
                    result[color] += int(value)
            self.rounds.append(result)
        self.maximums = defaultdict(lambda: 0)
        for r in self.rounds:
            for color, value in r.items():
                if self.maximums[color] < value:
                    self.maximums[color] = value


class Day2(Puzzle):
    day = 2

    def __init__(self, data=None):
        super().__init__(data=data)
        self.games: List[Game] = []
        self._parse_data()

    def _parse_data(self):
        for id, line in enumerate(self.data, 1):
            self.games.append(Game(id, line.split(": ")[1]))

    def part1(self):
        # only 12 red cubes, 13 green cubes, and 14 blue cubes
        def valid(g: Game):
            if (
                g.maximums["red"] > 12
                or g.maximums["green"] > 13
                or g.maximums["blue"] > 14
            ):
                return False
            else:
                return True

        valid_games = filter(valid, self.games)

        return sum([g.id for g in valid_games])

    def part2(self):
        return sum(
            [
                g.maximums["green"] * g.maximums["red"] * g.maximums["blue"]
                for g in self.games
            ]
        )
