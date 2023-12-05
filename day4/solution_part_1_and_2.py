from typing import List


class Card:

    def __init__(self):
        self.winning_numbers = []
        self.your_numbers = []
        self.score = 0
        self.win_count = 0
        self.copies = 1

    def __repr__(self):
        return f"score={self.score}, copies={self.copies}"

    def calculate_score(self):
        for number in self.your_numbers:
            if number in self.winning_numbers:
                self.score_up()

    def score_up(self):
        if self.score == 0:
            self.score = 1

        else:
            self.score *= 2

        self.win_count += 1


class Pile:
    def __init__(self, input_file):
        self.data = get_data(input_file)
        self.cards: List[Card] = []
        self.score = 0
        self.total_cards = 0

    def add_card(self, card: Card):
        self.cards.append(card)

    def read_card(self, line):
        card = Card()
        line = line.split(":")[1]
        winning_numbers, your_numbers = line.split("|")
        winning_numbers = winning_numbers.split()
        your_numbers = your_numbers.split()

        card.winning_numbers = winning_numbers
        card.your_numbers = your_numbers

        card.calculate_score()
        self.score += card.score

        self.add_card(card)


def get_data(data):
    with open(data, 'r') as f:
        lines = [line.strip() for line in f]

    return lines


def part2(pile: Pile):
    for i, card in enumerate(pile.cards):
        win_count = card.win_count
        for scoring_card in pile.cards[i+1: i+win_count+1]:
            scoring_card.copies += card.copies

        pile.total_cards += card.copies


def main():
    pile = Pile('input.txt')
    for card_data in pile.data:
        pile.read_card(card_data)

    part2(pile)

    print(f"Total score: {pile.score}")
    print("Total card count:", pile.total_cards)


if __name__ == '__main__':
    main()
