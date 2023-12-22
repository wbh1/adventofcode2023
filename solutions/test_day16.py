from solutions.day16 import Day16

data = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....""".splitlines()

d = Day16(data)

def test_part1():
    assert d.part1() == 46

def test_part2():
    assert d.part2() == 51
