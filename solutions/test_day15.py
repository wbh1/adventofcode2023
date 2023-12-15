from solutions.day15 import Day15

data = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7""".splitlines()

d = Day15(data=data)

def test_part1():
    assert d.part1() == 1320

def test_part2():
    assert d.part2() == 145
