from solutions.Puzzle import Puzzle
from typing import List, Tuple, Optional, Iterable


class Day13(Puzzle):
    day = 13

    def __init__(self, data=None):
        super().__init__(data)
        self.images: List[List[str]] = []
        cursor = 0
        for i, line in enumerate(self.data):
            if len(line) < 1:
                self.images.append(list(self.data[cursor:i]))
                cursor = i+1
        if any(self.data[cursor:]):
            self.images.append(self.data[cursor:])
        self.verticals = []
        self.horizontals = []

    @staticmethod
    def horizontal_reflection(image: List[Iterable], fix_smudges=False) -> Tuple[bool, Optional[int]]:
        for ri, row in enumerate(image[:len(image)-1]):
            a = image[max(0, (ri + 1) * 2 - len(image)) : ri + 1]
            b = image[ri + 1 : ri + len(a) + 1]
            b.reverse()
            assert len(a) == len(b)
            if fix_smudges:
                diffs = 0
                for i in range(0, len(a)):
                    for a1, b1 in zip(a[i], b[i]):
                        if a1 != b1:
                            diffs += 1
                    if diffs > 1:
                        break 
                if diffs == 1:
                    return (True, ri + 1)
            else:
                if a == b:
                    return (True, ri + 1)
        return (False, None)

    @staticmethod
    def vertical_reflection(image: List[str], fix_smudges=False) -> Tuple[bool, Optional[int]]:
        columns: List[List[str]] = [[] for r in range(0, len(image[0]))]
        for row in image:
            for i, c in enumerate(row):
                columns[i].append(c)
        return Day13.horizontal_reflection(columns, fix_smudges)

    def part1(self) -> int:
        verts = 0
        hors = 0
        for i in self.images:
            if (v := self.horizontal_reflection(i)) and v[0]:
                hors += v[1]
                self.horizontals.append(i)
            elif (v := self.vertical_reflection(i)) and v[0]:
                verts += v[1]
                self.verticals.append(i)
            else:
                raise ValueError("can't reflect!")

        return verts + (100 * hors)

    def part2(self) -> int:
        verts = 0
        hors = 0
        for i in self.images:
            if (v := self.horizontal_reflection(i, fix_smudges=True)) and v[0]:
                hors += v[1]
                self.horizontals.append(i)
            elif (v := self.vertical_reflection(i, fix_smudges=True)) and v[0]:
                verts += v[1]
                self.verticals.append(i)
            else:
                raise ValueError("can't reflect!")

        return verts + (100 * hors)
