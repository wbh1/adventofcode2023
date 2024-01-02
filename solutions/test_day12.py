import pytest
from solutions.day12 import matches, Day12

data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".splitlines()

d = Day12(data)

@pytest.mark.parametrize("text,expected", [
    ("???.### 1,1,3", 1),
    (".??..??...?##. 1,1,3", 4),
    ("?###???????? 3,2,1", 10)
])
def test_matches(text: str, expected: int):
    assert matches(text) == expected

@pytest.mark.parametrize("text,expected", [
    ("???.### 1,1,3", 1),
    (".??..??...?##. 1,1,3", 16384),
    ("?###???????? 3,2,1", 506250)
])
def test_matches_part2(text: str, expected: int):
    assert matches(text, copies=5) == expected

def test_part1():
    assert d.part1() == 21
