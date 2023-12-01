word_to_number = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open("input.txt") as f:
    lines = [line.strip() for line in f]

    calibration_sum = 0

    for line in lines:
        calibration_values = {}
        for i, character in enumerate(line):
            if character.isnumeric():
                calibration_values[i] = int(character)

        for word_number in word_to_number.keys():
            word_index_first = line.find(word_number)
            word_index_last = line.rfind(word_number)

            if word_index_first != -1:

                if word_index_first != word_index_last:
                    calibration_values[word_index_first] = word_to_number[word_number]
                    calibration_values[word_index_last] = word_to_number[word_number]
                else:
                    calibration_values[word_index_first] = word_to_number[word_number]

        calibration_values = [str(value) for key, value in sorted(calibration_values.items(), key=lambda x: x[0])]

        if len(calibration_values) < 2:
            calibration_value = int(calibration_values[0] * 2)

        else:
            first_digit = calibration_values[0]
            last_digit = calibration_values[-1]
            calibration_value = int(first_digit + last_digit)

        calibration_sum += calibration_value

print(f"Calibration sum: {calibration_sum}")