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
        for i, val in enumerate(self.instructions[0].split(":")[1].split(" ")[1:]):
            if i % 2 == 0:
                start = int(val)
            else:
                end = start + int(val)
                seed = Seed(start, end)
                self.seeds.append(seed)

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
        min_ranges = []
        for seed in self.seeds:
            for s_range in seed.ranges:
                min_ranges.append(s_range.start)

        return min(min_ranges)


class Seed:
    def __init__(self, start, end):
        self.ranges: List[range] = [range(start, end)]

    def __repr__(self):
        return f"seed range: {self.ranges}"

    def move_seed(self, new_loc, location_name):
        # self.history[location_name] = {self.loc: new_loc}
        # self.loc = new_loc
        pass


class SingleMap:
    def __init__(self, instruction):
        self.instruction = instruction.split(" ")
        self.source_range_start = int(self.instruction[0])
        self.dest_range_start = int(self.instruction[1])
        self.range_len = int(self.instruction[2])
        self.source_r = range(self.source_range_start, self.source_range_start + self.range_len)
        self.dest_r = range(self.dest_range_start, self.dest_range_start + self.range_len)

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
        leave_alone = []
        def split_range(seed_r, dest_r, source_r):
            new_ranges: List[range] = []
            old_ranges: List[range] = []
            start_dis = abs(seed_r.start - dest_r.start)
            end_dis = abs(seed_r.stop - dest_r.stop)

            if seed_r.start > dest_r.stop or seed_r.stop < dest_r.start:
                old_ranges.append(seed_r)

            elif seed_r.start < dest_r.start and seed_r.stop <= dest_r.stop:
                old_ranges.append(range(seed_r.start, dest_r.start-1)) # 1
                new_ranges.append(range(source_r.start, source_r.stop - end_dis))

            elif seed_r.start >= dest_r.start and seed_r.stop <= dest_r.stop:
                new_ranges.append(range(source_r.start + start_dis, source_r.stop - end_dis))

            elif seed_r.start >= dest_r.start and seed_r.stop > dest_r.stop:
                new_ranges.append(range(source_r.start + start_dis, source_r.stop))
                old_ranges.append(range(dest_r.stop+1, seed_r.stop))

            elif seed_r.start < dest_r.start and seed_r.stop > dest_r.stop:  # moga byc zle znaki
                new_ranges.append(range(source_r.start, source_r.stop))
                old_ranges = [range(seed_r.start, dest_r.start-1), range(dest_r.stop+1, seed_r.stop)]

            else:
                print("else")

            return new_ranges, old_ranges

        for single_map in self.maps:
            still_map = []
            for seed_range in seed.ranges:
                mapped_ranges_new, not_mapped_ranges_new = split_range(seed_range, single_map.dest_r, single_map.source_r)
                leave_alone.extend(mapped_ranges_new)
                still_map.extend(not_mapped_ranges_new)

            if still_map:
                seed.ranges = still_map
            else:
                break

        merged = leave_alone + still_map
        seed.ranges = merged



def main():
    almanac = Almanac('input.txt')
    almanac.get_seeds()
    almanac.get_maps()

    for seed in almanac.seeds:
        print(seed)
        for mapper in almanac.mappers:
            mapper.map_seed(seed)
            print("mapper done")

    print(f"Lowest location number is: {almanac.find_lowest_location()}")


if __name__ == '__main__':
    main()
