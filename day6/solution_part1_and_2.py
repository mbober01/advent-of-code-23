import math
from aoc_utils.data_utils import get_data


def boat_distance(race_time, best_distance):
    a = -1
    b = race_time
    c = -best_distance

    return a, b, c


def amount_of_solutions(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return 0
    elif delta == 0:
        return 1
    else:
        good_range = range(math.ceil((-b - delta**0.5) / (2*a)), math.floor((-b + delta**0.5) / (2*a)))
        return abs(int(good_range.stop+1) - int(good_range.start))


def parse_line(all_lines, index, part2=False):
    # index 0 for times and 1 for distances
    line = ' '.join(all_lines[index].split())
    if part2:
        return [line.split(":")[1][1:].replace(" ", "")]
    else:
        return line.split(":")[1][1:].split(" ")


def main():
    lines = get_data("input.txt")
    result = 1
    times = parse_line(lines, 0, part2=True)
    distances = parse_line(lines, 1, part2=True)

    for time, dist in zip(times, distances):
        a, b, c = boat_distance(int(time), int(dist))
        result *= amount_of_solutions(a, b, c)

    print(result)


if __name__ == "__main__":
    main()




