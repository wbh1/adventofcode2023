from solutions.Puzzle import Puzzle
from enum import IntEnum
from collections import Counter

HandType = IntEnum(
    "HandType", ["Five", "Four", "Full", "Three", "TwoPair", "OnePair", "HighCard"]
)
possible_cards = "AKQJT98765432"
possible_cards_jokers = "AKQT98765432J"


class Hand:
    def __init__(self, cards: str, bid: int, jokers_enabled=False) -> None:
        self.cards = cards
        self.bid = bid
        self.jokers = jokers_enabled
        self.hand = self.outcome()

    def outcome(self) -> HandType:
        cards = self.cards
        c = Counter(cards)
        if self.jokers and "J" in cards:
            joker_count = c.get("J", 0)
            # Don't delete the joker count if we only have jokers
            if joker_count < 5:
                del c["J"]
                # Add number of jokers to the most common card type
                c.update({c.most_common(1)[0][0]: joker_count})
        mc = c.most_common(2)
        if mc[0][1] == 5:
            return HandType.Five
        elif mc[0][1] == 4:
            return HandType.Four
        elif mc[0][1] == 3:
            if mc[1][1] == 2:
                return HandType.Full
            else:
                return HandType.Three
        elif mc[0][1] == 2 and mc[1][1] == 2:
            return HandType.TwoPair
        elif mc[0][1] == 2:
            return HandType.OnePair
        return HandType.HighCard

    def __eq__(self, other: object) -> bool:
        if other.hand == self.hand and other.cards == self.cards:
            return True
        return False

    def __lt__(self, other: object) -> bool:
        card_rank = possible_cards
        if self.jokers:
            card_rank = possible_cards_jokers
        if self.hand == other.hand:
            for c in zip(self.cards, other.cards):
                if c[0] != c[1]:
                    return card_rank.index(c[0]) < card_rank.index(c[1])
        else:
            return self.hand < other.hand


class Day7(Puzzle):
    day = 7

    def __init__(self, data=None):
        super().__init__(data)
        self.hands = []
        for line in self.data:
            x = line.split(" ")
            self.hands.append(Hand(x[0], int(x[1])))

    def part1(self) -> int:
        return sum(
            [h.bid * rank for rank, h in enumerate(sorted(self.hands, reverse=True), 1)]
        )

    def part2(self) -> int:
        self.hands = sorted(
            [Hand(h.cards, h.bid, jokers_enabled=True) for h in self.hands],
            reverse=True,
        )
        return sum([h.bid * rank for rank, h in enumerate(self.hands, 1)])
