from aoc_utils.data_utils import get_data


class Report:
    def __init__(self, input_data):
        history_rows = [history.split() for history in get_data(input_data)]
        self.histories = [History([int(num) for num in history]) for history in history_rows]


class History:
    def __init__(self, history):
        self.current_sequence = history
        self.last_values = []
        self.analyzer = Analyzer()

    def __repr__(self):
        return f'History({self.current_sequence})'

    def go_to_next(self):
        self.last_values.append(self.current_sequence[-1])
        self.current_sequence = self.analyzer.get_new_sequence(self.current_sequence)

    def go_max_depth(self):
        while not all([num == 0 for num in self.current_sequence]):
            self.go_to_next()

        self.last_values.append(0)


class Analyzer:
    def __init__(self):
        pass

    @staticmethod
    def get_new_sequence(sequence):
        new_sequence = []
        for index in range(len(sequence) - 1):
            new_number = sequence[index+1] - sequence[index]
            new_sequence.append(new_number)

        return new_sequence

    @staticmethod
    def predict_next_value(last_values):
        predicted_value = last_values[-1]
        for number in reversed(last_values[:-1]):
            predicted_value += number

        return predicted_value


def main():
    report = Report('input.txt')
    sum_of_predicted_values = 0
    for history in report.histories:
        history.go_max_depth()

        sum_of_predicted_values += history.analyzer.predict_next_value(history.last_values)

    print(sum_of_predicted_values)


if __name__ == '__main__':
    main()