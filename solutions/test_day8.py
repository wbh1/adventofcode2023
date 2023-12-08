from solutions.day8 import Day8

data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".splitlines()

data2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".splitlines()

data3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".splitlines()

d = Day8(data=data)
d2 = Day8(data=data2)
d3 = Day8(data=data3)

def test_part1():
    assert d.part1() == 2
    assert d2.part1() == 6

def test_part2():
    assert d3.part2() == 6
