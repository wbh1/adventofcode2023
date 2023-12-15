from solutions.Puzzle import Puzzle
from typing import List
from copy import copy


class Day14(Puzzle):
    day = 14

    def __init__(self, data=None):
        super().__init__(data)
        if not self.data:
            raise ValueError("Didn't parse data")
        self.current: List[str] = copy(self.data)

    def _tilt(self, step=1):
        """flips each item in the list from a row to a column
        Essentially a 90deg rotation
        """
        self.current = list(map("".join, zip(*self.current[::step])))

    def move(self, step=1):
        self._tilt(step)
        rotated = self.current
        for i in range(len(rotated)):
            for _ in range(len(rotated[i])):
                rotated[i] = rotated[i].replace(".O", "O.")
        return rotated

    def move_part2(
        self,
    ):
        self._tilt(step=-1)
        rotated = self.current
        for i in range(len(rotated)):
            for _ in range(len(rotated[i])):
                rotated[i] = rotated[i].replace("O.", ".O")
        return rotated

    def cycle(self, times=1, exp=[]) -> List[str]:
        # self.current = self.move()
        max = 100
        tilts = 0
        cycles = 0
        memory = {"".join(self.current): 1}
        cycle_start = 0
        for _ in range(times):
            for _ in range(4):
                self.current = self.move_part2()
                tilts += 1
            cycles += 1
            if (s := "".join(self.current)) and s in memory:
                cycle_start = memory[s]
                break
            else:
                memory[s] = cycles
        if cycles < times:
            cycle_length = cycles - cycle_start
            remaining = (times - cycle_start) % cycle_length
            print(
                f"found loop when the value from cycle {cycle_start} repeated in {cycles} (length {cycle_length}). need to do {remaining} more"
            )
            for _ in range(remaining):
                for _ in range(4):
                    self.current = self.move_part2()
                    tilts += 1
                cycles += 1
        return self.current

    def part1(self) -> int:
        return sum(
            i * (x == "O")
            for column in self.move()
            for i, x in enumerate(column[::-1], 1)
        )

    def part2(self, times=1000000000) -> int:
        self.current = copy(self.data)
        grid = self.cycle(times=times)
        return sum(r.count("O") * i for i, r in enumerate(grid[::-1], 1))
