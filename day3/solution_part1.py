from typing import List


class PartNumber:
    def __init__(self, value, start, end):
        self.part_number = value
        self.s_index = start
        self.e_index = end
        self.correct = False

    def __repr__(self):
        return f"Part number: {self.part_number}, [{self.s_index}, {self.e_index}], correct: {self.correct}"


class Symbol:
    def __init__(self, value, index, row_index):
        self.symbol = value
        self.index = index
        self.row_index = row_index

    def __repr__(self):
        return f"Symbol: {self.symbol}, [{self.index}]"


class Row:
    def __init__(self, line):
        self.line = line
        self.part_numbers: List[PartNumber] = []
        self.symbols: List[Symbol] = []

    def __repr__(self):
        return f"Part numbers: {self.part_numbers}, symbols: {self.symbols}"

    def get_part_numbers(self):
        part_number = None
        in_progress = False
        for i, char in enumerate(self.line):
            if char.isdigit() and not in_progress:
                part_number = PartNumber(char, i, i)
                self.part_numbers.append(part_number)
                in_progress = True

            elif char.isdigit() and in_progress:
                part_number.part_number += char

            elif not char.isdigit() and in_progress:
                in_progress = False
                part_number.e_index = i - 1

    def get_symbols(self, row_index):
        for i, char in enumerate(self.line):
            if not char.isdigit() and char != ".":
                symbol = Symbol(char, i, row_index)
                self.symbols.append(symbol)

    def get_data(self, row_index):
        self.get_part_numbers()
        self.get_symbols(row_index)

    def check_part_numbers(self, row_to_check):
        for part_number in self.part_numbers:
            for symbol in (row_to_check.symbols + self.symbols):
                if symbol.index in range(part_number.s_index-1, part_number.e_index+2):
                    part_number.correct = True
                    break
                else:
                    pass


class Schematic:
    def __init__(self, input_file):
        self.lines = []
        self.get_lines(input_file)
        self.part_num_sum = 0
        self.rows: List[Row] = []

    def get_lines(self, input_file):
        with open(input_file) as f:
            lines = [line.strip() for line in f]

        self.lines = lines

    def sum_correct_part_numbers(self):
        for row in self.rows:
            for part_number in row.part_numbers:
                if part_number.correct:
                    self.part_num_sum += int(part_number.part_number)


def main():
    schema = Schematic("input.txt")
    last_row = Row(None)
    for i, row in enumerate(schema.lines):
        row = Row(row)
        row.get_data(i)
        schema.rows.append(row)

        last_row.check_part_numbers(row)
        row.check_part_numbers(last_row)
        last_row = row

    schema.sum_correct_part_numbers()
    print(f"Sum of correct part numbers: {schema.part_num_sum}")


if __name__ == "__main__":
    main()
