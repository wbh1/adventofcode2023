from solutions.day11 import Day11
from itertools import combinations


data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".splitlines()

d = Day11(data=data)

def test_part1():
    res = d.part1()
    assert len(d.galaxies()) == 9
    combos = 0
    for _ in combinations(d.galaxies(), 2):
        combos += 1
    assert combos == 36

    assert res == 374

def test_part2():
    assert d.part2(10) == 1030
    assert d.part2(100) == 8410
