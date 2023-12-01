from solutions.day1 import Day1
import pytest

def test_part1():
    DATA = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()
    day = Day1(data=DATA)
    assert day.part1() == 142

def test_part2():
    DATA = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()
    day = Day1(data=DATA)
    assert day.part2() == 281

@pytest.mark.parametrize("test_input,expected",
                         [
                            ("lcsdjgkg4", 44),
                            ("sixxmfphssixninefivefive9fivefive", 65),
                            ("four52shspfjkppdng", 42),
                            ("8dp8fourhdcsmtfvxv", 84),
                            ("tqp8sevenkvvzpsxts6cqgmzzdxqvmeight2", 82),
                            ("36bpbjspbms8", 38),
                            ("nine8onehvbh", 91),
                            ("3kvrlxntlthfour", 34),
                            ("eightxvjtsevensevenpcrjtfcllzeight3mbjdjnklgxzzfdz", 83),
                            ("1fourtwo", 12),
                            ("qmlr5onegrcggpcsftmcphp", 51),
                            ("3ft49two", 32),
                            ("2xnsbrv9", 29),
                            ("lrcslkgkninehghhfive452zvlszp", 92),
                            ("fourtwoeight2one", 41),
                            ("6kjrcfivefqmtwoqrcpncpt2", 62),
                            ("rcdfk1eight1fournhzpvslq", 14),
                            ("sztlrrktt4four5onesbjvd", 41),
                            ("qdp3", 33),
                            ("vdmcnjkqjvn6fxnmzdrmsgbm", 66),
                            ("lhmonegqddt7sixrxcqpfbdfvbgrhjhf", 16),
                            ("sixone8", 68),
                            ("9bdgczsxq6four", 94),
                            ("keightwo1cmlshtwofourksgbvfxvb", 84),
                            ("sevenine", 79),
                            ("eighthree", 83),
                            ("""qmlr5onegrcggpcsftmcphp
3ft49two
2xnsbrv9
lrcslkgkninehghhfive452zvlszp
fourtwoeight2one
6kjrcfivefqmtwoqrcpncpt2
rcdfk1eight1fournhzpvslq
sztlrrktt4four5onesbjvd
qdp3
vdmcnjkqjvn6fxnmzdrmsgbm
lhmonegqddt7sixrxcqpfbdfvbgrhjhf
sixone8
9bdgczsxq6four
keightwo1cmlshtwofourksgbvfxvb""", 723)
                         ])
def test_part2_parsing(test_input, expected):
    DATA = test_input.splitlines()
    day = Day1(data=DATA)
    assert day.part2() == expected
