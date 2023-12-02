from solution_part1 import GamePart1


class GamePart2(GamePart1):
    def __init__(self, game):
        super().__init__(game)

    def get_set_power(self):
        set_power = 1
        for color, count in self.highest_counts.items():
            set_power *= count

        return set_power


def main():
    with open("input.txt") as f:
        games = [game.strip() for game in f]
        set_powers = []
        for game in games:
            game = GamePart2(game)
            for i in range(len(game.sets)):
                game.get_set()

            set_powers.append(game.get_set_power())

        print(f"sum of set powers: {sum(set_powers)}")


if __name__ == "__main__":
    main()
