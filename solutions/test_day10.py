from solutions.day10 import Day10

def test_simple_loop():
    data = """.....
.S-7.
.|.|.
.L-J.
.....""".splitlines()
    d = Day10(data)
    assert d.part1() == 4

def test_complex_loop():
    data = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...""".splitlines()
    d = Day10(data)
    assert d.part1() == 8

def test_part2_loop():
    data = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...""".splitlines()
    
    d = Day10(data)
    assert 8 == d.part2()
