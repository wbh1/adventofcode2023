from solutions.day6 import Day6

data = """Time:      7  15   30
Distance:  9  40  200""".splitlines()

d = Day6(data=data)

def test_part1():
    assert d.part1() == 288

def test_part2():
    assert d.part2() == 71503
