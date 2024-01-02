from copy import copy
from itertools import chain
from typing import Dict, List, Tuple

from solutions.Puzzle import Puzzle


def matches(s: str, copies=1) -> int:
    line = s.split(" ")
    springs = line[0]
    groups = [int(i) for i in line[1].split(",")]
    if copies > 1:
        new_string = copy(springs)
        for _ in range(copies - 1):
            new_string += f"?{springs}"
        springs = new_string
        new_groups = [groups] * copies
        groups = list(chain(*new_groups))

    states, states_dict = nfa(springs, groups)
    return states_dict.get(len(states) - 1, 0) + states_dict.get(len(states) - 2, 0)


# non-deterministic finite automata
# inspired by https://github.com/clrfl/AdventOfCode2023/blob/cc9b53f6cee9560449b40eb63222d276a7a8f4f7/12/explanation.ipynb
def nfa(text: str, groups: List[int]) -> Tuple[str, Dict[int, int]]:
    states = "."
    # populate the states that we need to match
    for g in groups:
        for i in range(g):
            states += "#"
        states += "."

    # initial states with only 1 way to match starting at state 0
    states_dict = {0: 1}
    new_dict = {}
    for spring in text:
        for state in states_dict.keys():
            if spring == "?":
                if state + 1 < len(states):
                    new_dict[state + 1] = (
                        new_dict.get(state + 1, 0) + states_dict[state]
                    )
                if states[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + states_dict[state]

            elif spring == ".":
                if state + 1 < len(states) and states[state + 1] == ".":
                    new_dict[state + 1] = (
                        new_dict.get(state + 1, 0) + states_dict[state]
                    )
                if states[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + states_dict[state]

            elif spring == "#":
                if state + 1 < len(states) and states[state + 1] == "#":
                    new_dict[state + 1] = (
                        new_dict.get(state + 1, 0) + states_dict[state]
                    )

        states_dict = new_dict
        new_dict = {}

    return (states, states_dict)


class Day12(Puzzle):
    day = 12

    def __init__(self, data=None):
        super().__init__(data)

    def part1(self) -> int:
        return sum(matches(s) for s in self.data)

    def part2(self) -> int:
        return sum(matches(s, copies=5) for s in self.data)
