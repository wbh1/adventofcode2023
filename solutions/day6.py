from solutions.Puzzle import Puzzle
import re

numbers = re.compile(r"(\d+)")

class Day6(Puzzle):
    day = 6
    
    def __init__(self, data=None):
        super().__init__(data)
        self.times = [int(x.group(0)) for x in numbers.finditer(self.data[0])]
        self.distances = [int(x.group(0)) for x in numbers.finditer(self.data[1])]
    
    def part1(self) -> int:
        margins_of_error = []
        for race in zip(self.times, self.distances):
            min_hold = 1
            max_hold = race[0] - 1
            for button_hold in range(0, race[0]):
                if (button_hold * (race[0] - button_hold)) > race[1]:
                    min_hold = button_hold
                    break
            for button_hold in range(race[0]-1, 0, -1):
                if (button_hold * (race[0] - button_hold)) > race[1]:
                    max_hold = button_hold
                    break
            margins_of_error.append(max_hold-min_hold+1)
        res = 1
        for x in margins_of_error:
            res *= x
        return res

    def part2(self) -> int:
        time = int("".join(str(x) for x in self.times))
        distance = int("".join(str(x) for x in self.distances))
        race = (time, distance)
        min_hold = 1
        max_hold = race[0] - 1
        for button_hold in range(0, race[0]):
            if (button_hold * (race[0] - button_hold)) > race[1]:
                min_hold = button_hold
                break
        for button_hold in range(race[0]-1, 0, -1):
            if (button_hold * (race[0] - button_hold)) > race[1]:
                max_hold = button_hold
                break
        return max_hold - min_hold + 1

            

            


