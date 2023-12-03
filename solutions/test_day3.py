from solutions.day3 import Day3

data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".splitlines()

d = Day3(data=data)

def test_part1():
    r = d.part1()
    assert r == 4361

def test_part2():
    d.part1()
    r = d.part2()
    assert r == 467835
