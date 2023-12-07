from __future__ import annotations

from typing import List
from enum import Enum
from collections import Counter

from aoc_utils.data_utils import get_data


class TypeStrength(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


class HandStrength:
    card_mapping = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 1,
        "T": 10,
    }

    def __init__(self, hand_type: TypeStrength, cards):
        self.type_strength: int = hand_type.value
        self.cards_strength: List[int] = self.get_cards_strength(cards)

    def __repr__(self):
        return f"HandStrength({self.type_strength}, {self.cards_strength})"

    def get_cards_strength(self, cards):
        return [self.card_mapping[card] if card in self.card_mapping.keys() else int(card) for card in cards]

    def __eq__(self, other: HandStrength):
        return (self.type_strength == other.type_strength
                and
                all([card1 == card2 for card1, card2 in zip(self.cards_strength, other.cards_strength)]))

    def __lt__(self, other: HandStrength):
        if self.type_strength == other.type_strength:
            for card1, card2 in zip(self.cards_strength, other.cards_strength):
                if card1 == card2:
                    continue
                return card1 < card2

        return self.type_strength < other.type_strength


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.hand_strength: HandStrength = self.get_hand_strength()

    def __repr__(self):
        return f"Hand({self.cards}, {self.bid}, {self.hand_strength})"

    def __eq__(self, other: Hand):
        return self.hand_strength == other.hand_strength

    def __lt__(self, other: Hand):
        return self.hand_strength < other.hand_strength

    @staticmethod
    def find_most_common_card(card_count):
        most_common_card = None
        max_count = 0
        for card in set(card_count.keys()):
            if card != "J":
                if card_count[card] > max_count:
                    max_count = card_count[card]
                    most_common_card = card

        return most_common_card

    def get_hand_strength(self):
        card_count = Counter(self.cards)

        joker_count = card_count["J"]
        most_common_card = self.find_most_common_card(card_count)
        card_count[most_common_card] += joker_count
        card_count.pop("J", None)

        if len(card_count) == 1 or len(card_count) == 0:
            hand_type = TypeStrength.FIVE_OF_A_KIND
        elif len(card_count) == 2:
            if 4 in card_count.values():
                hand_type = TypeStrength.FOUR_OF_A_KIND
            else:
                hand_type = TypeStrength.FULL_HOUSE
        elif len(card_count) == 3:
            if 3 in card_count.values():
                hand_type = TypeStrength.THREE_OF_A_KIND
            else:
                hand_type = TypeStrength.TWO_PAIR
        elif len(card_count) == 4:
            hand_type = TypeStrength.ONE_PAIR
        else:
            hand_type = TypeStrength.HIGH_CARD

        return HandStrength(hand_type, self.cards)


class AllHands:
    def __init__(self, input_data):
        self.hands: List[Hand] = [Hand(hand.split(" ")[0], hand.split(" ")[1]) for hand in get_data(input_data)]

    def __repr__(self):
        return f"AllHands({self.hands})"

    def winnings(self):
        wins = 0
        for rank, hand in enumerate(self.hands):
            wins += (rank+1) * int(hand.bid)

        return wins


def main():
    all_hands = AllHands("input.txt")
    all_hands.hands.sort()

    print(all_hands.winnings())



if __name__ == "__main__":
    main()