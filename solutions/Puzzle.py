class Puzzle:
    day = 0
    def __init__(self, data=None):
        if data is not None:
            self.data = data
            return

        with open(f"inputs/day{self.day}.txt") as f:
            self.data = f.read().splitlines()

    def part1(self) -> int:
        pass

    def part2(self) -> int:
        pass

    def solve(self):
        print("Part 1:", self.part1())
        print("Part 2:", self.part2())
