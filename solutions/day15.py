from solutions.Puzzle import Puzzle
from collections import OrderedDict


class Day15(Puzzle):
    day = 15

    def __init__(self, data=None):
        super().__init__(data)
        assert len(self.data) == 1
        self.input = self.data[0].split(",")
        self.boxes = {}

    def hash(self, s: str) -> int:
        current_value = 0
        for c in s:
            current_value += ord(c)
            current_value = current_value * 17
            current_value = current_value % 256

        return current_value

    def focusing_power(self, box: int, slot: int, focal_length: int) -> int:
        return (1 + box) * slot * focal_length

    def part1(self) -> int:
        return sum([self.hash(s) for s in self.input])

    def part2(self) -> int:
        for s in self.input:
            if "=" in s:
                split = s.split("=")
                label = split[0]
                box = self.hash(label)
                focal_length = int(split[1])
                if self.boxes.get(box):
                    self.boxes[box][label] = focal_length
                else:
                    self.boxes[box] = OrderedDict({label: focal_length})
            elif "-" in s:
                label = s.strip("-")
                box = self.hash(label)
                try:
                    self.boxes[box].pop(label)
                except KeyError:
                    continue
        power = 0
        for boxid, box in self.boxes.items():
            for slot, lens in enumerate(box.values(), 1):
                power += self.focusing_power(boxid, slot, lens)
        return power
