from solutions.day5 import Day5, Seed


data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".split("\n\n")

d = Day5(data=data)

def test_part1():
    assert len(d.data) == 8
    assert [x.number for x in d.seeds] == [79, 14, 55, 13]
    seed1 = d.seeds[0]
    assert seed1.soil == 81
    assert seed1.fertilizer == 81
    assert seed1.water == 81
    assert seed1.light == 74
    assert seed1.temperature == 78
    assert seed1.humidity == 78
    assert seed1.location == 82

    assert d.part1() == 35

def test_part2():
    s = d.part2()
    assert s == 46

def test_location():
    assert 79 == Seed.loc_to_seed(82)
    s = Seed(55)
    assert 55 == Seed.loc_to_seed(s.location)
