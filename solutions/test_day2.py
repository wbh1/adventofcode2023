from solutions.day2 import Day2
import pytest

@pytest.fixture
def day2():
    DATA = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()
    return Day2(data=DATA)

def test_part1(day2):
    assert day2.games[0].rounds[0] == {"blue": 3, "red": 4, "green": 0}
    assert day2.games[0].rounds[1] == {"blue": 6, "red": 1, "green": 2}
    assert day2.games[0].rounds[2] == {"blue": 0, "red": 0, "green": 2}

    assert day2.part1() == 8

def test_part2(day2):
    assert day2.part2() == 2286
