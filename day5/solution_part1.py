from typing import List

from aoc_utils.data_utils import get_data


class Almanac:
    def __init__(self, input_data):
        self.instructions = get_data(input_data)
        self.seeds: List[Seed] = []
        self.mappers: List[Mapper] = []

    def __repr__(self):
        return f"seeds: {self.seeds}"

    def get_seeds(self):
        self.seeds = [Seed(int(val)) for val in self.instructions[0].split(":")[1].split(" ")[1:]]

    def get_maps(self):
        mapper = Mapper()

        for instruction in self.instructions[2:]:
            if "map" in instruction:
                mapper_name = instruction.split(" ")[0].split("-")[-1]
                mapper.name = mapper_name

            elif instruction == "":
                self.mappers.append(mapper)
                mapper = Mapper()

            else:
                new_map = SingleMap(instruction)
                mapper.maps.append(new_map)

        self.mappers.append(mapper)

    def find_lowest_location(self):
        return min([seed.loc for seed in self.seeds])


class Seed:
    def __init__(self, value):
        self.source_loc = value
        self.loc = value
        self.history = {"seed": value}

    def __repr__(self):
        return f"Seed(source_loc={self.source_loc}, loc={self.loc}, history={self.history})"

    def move_seed(self, new_loc, location_name):
        self.history[location_name] = {self.loc: new_loc}
        self.loc = new_loc


class SingleMap:
    def __init__(self, instruction):
        self.instruction = instruction.split(" ")
        self.source_range_start = int(self.instruction[0])
        self.dest_range_start = int(self.instruction[1])
        self.range_len = int(self.instruction[2])

    def __repr__(self):
        return (f"SingleMap(dest_range_start={self.dest_range_start}, source_range_start={self.source_range_start},"
                f" range_len={self.range_len}")


class Mapper:
    def __init__(self):
        self.name = ""

        self.maps: List[SingleMap] = []

    def __repr__(self):
        return f"Mapper(name={self.name}, maps={self.maps})"

    def map_seed(self, seed: Seed):
        for single_map in self.maps:
            seed_dist = seed.loc - single_map.dest_range_start
            if single_map.range_len > seed_dist >= 0:
                return single_map.source_range_start + seed_dist

        return seed.loc


def main():
    almanac = Almanac('input.txt')
    almanac.get_seeds()
    almanac.get_maps()

    for seed in almanac.seeds:

        for mapper in almanac.mappers:
            new_loc = mapper.map_seed(seed)
            seed.move_seed(new_loc, mapper.name)

        print(seed)

    print(f"Lowest location number is: {almanac.find_lowest_location()}")


if __name__ == '__main__':
    main()
