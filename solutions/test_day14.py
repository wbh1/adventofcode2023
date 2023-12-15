from solutions.day14 import Day14
import pytest

data = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".splitlines()


d = Day14(data=data)

def test_part1():
    assert d.part1() == 136

def test_part1b():
    grid = d.move_part2()
    assert sum(i*(x == 'O') for column in grid for i, x in enumerate(column, 1)) == 136
    # assert sum(r.count("O") * i for i, r in enumerate(grid[::-1], 1)) == 136

def test_1cycle():
    exp = """.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....""".splitlines()
    # exp = list(map(''.join, zip(*exp)))
    assert d.cycle() == exp
    assert sum(r.count("O") * i for i, r in enumerate(exp[::-1], 1)) == 87

def test_2cycles():
    exp = """.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O""".splitlines()
    assert d.cycle(2) == exp
    assert sum(r.count("O") * i for i, r in enumerate(exp[::-1], 1)) == 69

def test_3cycles():
    exp = """.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O""".splitlines()
    assert d.cycle(3) == exp
    assert sum(r.count("O") * i for i, r in enumerate(exp[::-1], 1)) == 69

def test_part2():
    assert d.part2() == 64

@pytest.mark.parametrize("cycles,exp", [
    (1, 87),
    (2, 69),
    (3, 69),
    (4, 69),
    (5, 65),
    (6, 64),
    (7, 65),
    (8, 63),
    (9, 68),
    (10, 69),
])
def test_part2_cycles(exp, cycles):
    day = Day14(data=data)
    assert day.part2(cycles) == exp
