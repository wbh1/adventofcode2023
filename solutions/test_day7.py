from solutions.day7 import Day7


data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()
d = Day7(data=data)

alt_data = """2345A 1
Q2KJJ 13
Q2Q2Q 19
T3T3J 17
T3Q33 11
2345J 3
J345A 2
32T3K 5
T55J5 29
KK677 7
KTJJT 34
QQQJA 31
JJJJJ 37
JAAAA 43
AAAAJ 59
AAAAA 61
2AAAA 23
2JJJJ 53
JJJJ2 41""".splitlines()

d2 = Day7(data=alt_data)

def test_part1():
    assert d.part1() == 6440

def test_part2():
    order = ['32T3K', 'KK677', 'T55J5', 'QQQJA', 'KTJJT']
    res = d.part2()
    assert order == [c.cards for c in d.hands]
    assert res == 5905

def test_part2_alt():
    res = d2.part2()
    assert res == 6839
