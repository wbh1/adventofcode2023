from solutions.day9 import Day9

data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()
d = Day9(data=data)


def test_part1():
    assert Day9.extrapolate(d.data[0]) == 18
    assert Day9.extrapolate(d.data[1]) == 28
    assert Day9.extrapolate(d.data[2]) == 68
    assert d.part1() == 114

def test_part2():
    assert d.part2() == 2
