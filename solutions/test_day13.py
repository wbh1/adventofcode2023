from solutions.day13 import Day13


data = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".splitlines()

h = """#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".splitlines()

v = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.""".splitlines()

d = Day13(data=data)

def test_horizontal():
    # res = d.horizontal_reflection(h)
    # assert res[0] is True
    # assert res[1] == 4

    assert d.horizontal_reflection(v)[0] is False

def test_vertical():
    res = d.vertical_reflection(v)
    assert res[0] is True
    assert res[1] == 5

def test_input():
    assert len(d.images) == 2

def test_part1():
    assert d.part1() == 405

def test_vertical_smudge():
    res = d.horizontal_reflection(v, fix_smudges=True)
    assert res[0] is True
    assert res[1] == 3

def test_horizontal_smudge():
    res = d.horizontal_reflection(h, fix_smudges=True)
    assert res[0] is True
    assert res[1] == 1

def test_part2():
    d.part1()
    assert d.part2() == 400
