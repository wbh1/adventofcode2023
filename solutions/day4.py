from solutions.Puzzle import Puzzle
import re
from dataclasses import dataclass
from typing import List
from itertools import chain

prefix = re.compile(r"Card (\d)+:")

@dataclass
class Card:
    id : int
    matches : int

    def points(self):
        if self.matches > 0:
            return 2**(self.matches-1)
        else:
            return 0

class Day4(Puzzle):
    
    day = 4

    cards : List[Card] = []

    def part1(self):
        line: str
        points = 0
        for id, line in enumerate(self.data):
            line = line.split(":")[1]
            winners, mine = line.split("|")

            winners = set(x for x in winners.strip().split(" ") if x)
            mine = set(x for x in mine.strip().split(" ") if x)
            
            matches = 0
            for n in winners:
                if n in mine:
                    matches += 1
            self.cards.append(Card(id+1, matches))
        
        for c in self.cards:
            points += c.points()
        
        return points
    
    def _winning_scratchers(self, c: Card) -> List[Card]:
        if c.matches > 0:
            new_cards = self.cards[c.id:c.id+c.matches]
            return new_cards + list(chain(*[self._winning_scratchers(card) for card in new_cards]))
        else:
            return []
            
    
    def part2(self):
        if len(self.cards) == 0:
            self.part1()
        for c in self.cards:
            self.cards = self.cards + self._winning_scratchers(c)

        return len(self.cards)
            

            