from typing import AnyStr, List, Optional, Tuple

from solutions.Puzzle import Puzzle


class Day13(Puzzle):
    day = 13

    def __init__(self, data=None):
        super().__init__(data)
        self.images: List[List[str]] = []
        cursor = 0
        # Iterate over the data, which is already split by line
        # but we need to identify empty lines that separate images
        for i, line in enumerate(self.data):
            if len(line) < 1:
                self.images.append(list(self.data[cursor:i]))
                cursor = i + 1
        # if there's any remaining non-empty data that hasn't been added
        # as an image yet, add it now
        if any(self.data[cursor:]):
            self.images.append(self.data[cursor:])

    @staticmethod
    def horizontal_reflection(
        image: List[AnyStr], fix_smudges=False
    ) -> Tuple[bool, Optional[int]]:
        for ri, row in enumerate(image[: len(image) - 1]):
            a = image[max(0, (ri + 1) * 2 - len(image)) : ri + 1]
            b = image[ri + 1 : ri + len(a) + 1]
            # to be a reflection, the order of entries in b should be the inverse of a
            # i.e. a's last item should be b's first, and so on
            b.reverse()
            assert len(a) == len(b)
            # if we're doing part 2, identify where a and b only have
            # one different character between the two of them
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
    def vertical_reflection(
        image: List[AnyStr], fix_smudges=False
    ) -> Tuple[bool, Optional[int]]:
        """vertical_reflection works by changing the list of row
        to a list of columns and then applying horizontal reflection.
        Think of it as rotating the image 90 degrees so that the vertical
        line of reflection is now a horizontal line.
        """
        columns: List[str] = ["" for r in range(0, len(image[0]))]
        for row in image:
            for i, c in enumerate(row):
                columns[i] += str(c)
        return Day13.horizontal_reflection(columns, fix_smudges)

    def process(self, **kwargs) -> int:
        verts = 0
        hors = 0
        for i in self.images:
            if (
                (v := self.horizontal_reflection(i, **kwargs))
                and v[0]
                and v[1] is not None
            ):
                hors += v[1]
            elif (
                (v := self.vertical_reflection(i, **kwargs))
                and v[0]
                and v[1] is not None
            ):
                verts += v[1]
            else:
                raise ValueError("can't reflect!")

        return verts + (100 * hors)

    def part1(self) -> int:
        return self.process()

    def part2(self) -> int:
        return self.process(fix_smudges=True)
