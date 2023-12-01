with open("input.txt") as f:
    lines = [line.strip() for line in f]

    calibration_sum = 0

    for line in lines:
        calibration_values = [character for character in line if character.isnumeric()]

        first_digit = calibration_values[0]
        last_digit = calibration_values[-1]
        calibration_value = int(first_digit + last_digit)

        calibration_sum += calibration_value


print(f"Calibration sum: {calibration_sum}")