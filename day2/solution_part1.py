class GamePart1:
    def __init__(self, game):
        self.possible_counts = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }

        self.highest_counts = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        self.game_line = game
        self.game_num = self.get_game_num()
        self.sets = self.get_sets()
        self.current_set = 0

        self.game_valid = True

    def __repr__(self):
        return f"Game {self.game_num}, {self.highest_counts}, game_valid: {self.game_valid}"

    def get_game_num(self):
        game_num = self.game_line.split(":")[0].split(" ")[1]
        self.game_line = self.game_line.split(":")[1]
        return game_num

    def check_if_higher(self, color, count):
        if count > self.highest_counts[color]:
            self.highest_counts[color] = count

    def get_sets(self):
        sets = self.game_line.split(";")
        return sets

    def get_set(self):
        color_rolls = self.sets[self.current_set].split(",")
        for color_roll in color_rolls:
            roll, color = color_roll.split(" ")[1:]
            self.check_if_higher(color, int(roll))

        self.current_set += 1

    def check_if_game_valid(self):
        for color, count in self.highest_counts.items():
            if count > self.possible_counts[color]:
                self.game_valid = False


def main():
    with open("input.txt") as f:
        valid_game_nums_sum = 0
        games = [game.strip() for game in f]
        for game in games:
            game = GamePart1(game)
            for i in range(len(game.sets)):
                game.get_set()

            game.check_if_game_valid()

            if game.game_valid:
                valid_game_nums_sum += int(game.game_num)

        print(f"sum of game ids which were valid: {valid_game_nums_sum}")


if __name__ == "__main__":
    main()



