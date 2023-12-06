from solutions.Puzzle import Puzzle
from multiprocessing import Process, Pipe
import multiprocessing
from multiprocessing.connection import Connection
from typing import List, Dict
import re

multiprocessing.set_start_method("fork")
regex = re.compile(r"(\d+) (\d+) (\d+)")

maps: Dict[str, List[Dict[str, int]]] = {}


class Seed:
    number: int
    soil: int
    fertilizer: int
    water: int
    light: int
    temperature: int
    humidity: int
    location: int

    def __init__(self, number: int) -> None:
        self.number = number
        self.soil = self._map("seed-to-soil", self.number)
        self.fertilizer = self._map("soil-to-fertilizer", self.soil)
        self.water = self._map("fertilizer-to-water", self.fertilizer)
        self.light = self._map("water-to-light", self.water)
        self.temperature = self._map("light-to-temperature", self.light)
        self.humidity = self._map("temperature-to-humidity", self.temperature)
        self.location = self._map("humidity-to-location", self.humidity)

    def _map(self, map_name: str, src_attribute: int) -> int:
        for map in maps[map_name]:
            if map["src_start"] <= src_attribute <= map["src_start"] + map["length"]:
                return map["dest_start"] + (src_attribute - map["src_start"])
        return src_attribute

    @staticmethod
    def loc_to_seed(loc: int) -> int:
        src_attribute = loc
        for m in list(maps.keys())[::-1]:
            for map in maps[m]:
                if (
                    map["dest_start"]
                    <= src_attribute
                    < map["dest_start"] + map["length"]
                ):
                    src_attribute = map["src_start"] + (
                        src_attribute - map["dest_start"]
                    )
                    break

        return src_attribute

    def _set_soil(self) -> None:
        self.soil = self._map("seed-to-soil", self.number)


class Day5(Puzzle):
    day = 5
    seeds: List[Seed] = []

    def __init__(self, data=None):
        if data is not None:
            self.data = data
        else:
            with open(f"inputs/day{self.day}.txt") as f:
                self.data = f.read().split("\n\n")

        for map in self.data[1:]:
            m = map.split(" map:\n")
            maps[m[0]] = [
                {
                    "dest_start": int(d.group(1)),
                    "src_start": int(d.group(2)),
                    "length": int(d.group(3)),
                }
                for d in regex.finditer(m[1])
            ]

        self.seeds = [Seed(int(i)) for i in self.data[0].split(": ")[1].split(" ")]

    def part1(self) -> int:
        return min([s.location for s in self.seeds])

    def run(self, s: int, e: int, c: Connection):
        for loc in range(s, e):
            if c.closed:
                return
            seed = Seed.loc_to_seed(loc)
            for start, length in zip(self.seeds[::2], self.seeds[1::2]):
                if start.number <= seed < (start.number + length.number):
                    c.send(loc)
                    c.close()

    def part2(self) -> int:
        p, c = Pipe()

        step = 4000000
        processes = [
            Process(target=self.run, args=(loc, loc + step, c))
            for loc in range(0, 12634634, step)
        ]
        for subp in processes:
            subp.start()
        answer = p.recv()
        for subp in processes:
            subp.terminate()
        p.close()
        return answer
