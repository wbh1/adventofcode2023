from solutions.Puzzle import Puzzle
from collections import defaultdict
import re

# delta row / delta column
# right, left, up, down, up-left, up-right, down-left, down-right (respectively)
# modified from day15, 2021
DR = [0, 0, -1, 1, -1, -1, 1, 1]
DC = [1, -1, 0, 0, -1, 1, -1, 1]

class Day3(Puzzle):
    day = 3
    symbol_regex = re.compile(r"([^\w\.\n])")
    part_numbers = []
    gears = defaultdict(lambda: [])
    def part1(self):
        number_regex = re.compile(r"(\d+)")
        for ri, row in enumerate(self.data):
            for number in number_regex.finditer(row):
                points = [(x, ri) for x in range(number.regs[0][0], number.regs[0][1])]
                counted = False
                adj_gears = set()
                for p in points:
                    if symbols := self.should_count(p):
                        if symbols:
                            if not counted:
                                self.part_numbers.append(int(number.group(0)))
                                counted = True
                            for s in symbols:
                                if s[0] == "*":
                                    adj_gears.add(s[1])
                for g in adj_gears:
                    self.gears[g].append(int(number.group(0)))
                        
        return sum(self.part_numbers)
    
    def part2(self):
        gear_ratios = []
        for adj_nums in self.gears.values():
            if len(adj_nums) > 2 or len(adj_nums) < 2:
                continue 
            gear_ratios.append(adj_nums[0] * adj_nums[1])
        return sum(gear_ratios)


    
    # Modified based on day15 2021
    def should_count(self, point: tuple) -> bool:
        x, y = point
        adj_symbols = []
        for i in range(0, 8):
            if 0 <= y + DR[i] < len(self.data) and 0 <= x + DC[i] < len(self.data[0]):
                s = self.symbol_regex.search(self.data[y + DR[i]][x + DC[i]])
                if s is not None:
                    adj_symbols.append((s.group(0), (x + DC[i], y + DR[i])))
        return adj_symbols
