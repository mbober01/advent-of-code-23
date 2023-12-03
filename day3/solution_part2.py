from typing import List, Tuple

from solution_part1 import PartNumber, Symbol, Row, Schematic


class PartNumber2(PartNumber):
    def __init__(self, value, start, end):
        super().__init__(value, start, end)
        self.gear: Symbol2 = Symbol2(None, None, None)

    def __repr__(self):
        return f"Part number: {self.part_number}, [{self.s_index}, {self.e_index}], correct: {self.correct}, gear: {self.gear}"


class Symbol2(Symbol):
    def __init__(self, value, index, row_index):
        super().__init__(value, index, row_index)

    def __repr__(self):
        return f"index: {self.index}, row_index: {self.row_index}"


class Row2(Row):
    def __init__(self, line, schema):
        super().__init__(line)
        self.part_numbers: List[PartNumber2] = []
        self.schema = schema

    def get_part_numbers(self):
        part_number = None
        in_progress = False
        for i, char in enumerate(self.line):
            if char.isdigit() and not in_progress:
                part_number = PartNumber2(char, i, i)
                self.part_numbers.append(part_number)
                in_progress = True

            elif char.isdigit() and in_progress:
                part_number.part_number += char

            elif not char.isdigit() and in_progress:
                in_progress = False
                part_number.e_index = i - 1

    def get_symbols(self, row_index):
        for i, char in enumerate(self.line):
            if char == "*":
                symbol = Symbol2(char, i, row_index)
                self.symbols.append(symbol)

    def check_part_numbers(self, row_to_check):
        for part_number in self.part_numbers:
            for symbol in (row_to_check.symbols + self.symbols):
                if symbol.index in range(part_number.s_index-1, part_number.e_index+2):
                    part_number.correct = True
                    part_number.gear = symbol

                    if part_number not in self.schema.correct_part_numbers:
                        self.schema.correct_part_numbers.append(part_number)

                    break
                else:
                    pass


class Schematic2(Schematic):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.rows: List[Row2] = []
        self.correct_part_numbers: List[PartNumber2] = []

    def sum_correct_part_numbers(self):
        for i, part_number in enumerate(self.correct_part_numbers):
            for second_number in self.correct_part_numbers[i+1:]:
                if part_number.gear == second_number.gear:
                    self.part_num_sum += int(part_number.part_number) * int(second_number.part_number)
                    print(f"Part numbers: {part_number.part_number}, {second_number.part_number}")
                    break


def main():
    schema = Schematic2("input.txt")
    last_row = Row2(None, schema)
    for i, row in enumerate(schema.lines):
        row = Row2(row, schema)
        row.get_data(i)
        schema.rows.append(row)

        last_row.check_part_numbers(row)
        row.check_part_numbers(last_row)
        last_row = row

    for part_number in schema.correct_part_numbers:
        print(part_number)

    schema.sum_correct_part_numbers()
    print(f"Sum of correct part numbers: {schema.part_num_sum}")


if __name__ == "__main__":
    main()